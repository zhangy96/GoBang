# -*- coding: utf-8 -*-
__author__ = 'gzs2473'

import socket
import json
import select
import Queue
import logging
import sqlite3

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s:\t%(message)s',
                        datefmt='[%Y-%m-%d %H:%M:%S]')
player_info = {}
tables = [([0] * 2) for i in range(16)]

db = sqlite3.connect('server/gobang.db')
cursor = db.cursor()


class State(object):
    IN_ROOM = 1
    IN_TABLE = 2
    PREPARED = 3
    PLAYING = 4

###########################################################
#service基类
###########################################################
class Service(object):
    def __init__(self, sid, ser):
        self.server = ser
        self.service_id = sid
        self.__command_map = {}

    def handle(self, msg, sender):
        cid = msg['cid']
        if not cid in self.__command_map:
            logging.error('bad command %s' % cid)
        f = self.__command_map[cid]
        return f(msg, sender)

    def register(self, cid, function):
        self.__command_map[cid] = function

    def registers(self, command_dict):
        for cid in command_dict:
            self.register(cid, command_dict[cid])

###########################################################
# 负责用户登录/退出的服务sid=2000
# cid=1001：用户登录
# cid=1002：用户退出
###########################################################
class LoginService(Service):
    SERVICE_ID = 2000

    def __init__(self, ser):
        super(LoginService, self).__init__(LoginService.SERVICE_ID, ser)
        commands = {
            1001: self.handle_login,
            1002: self.handle_logout
        }
        self.registers(commands)

    def handle_login(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        logging.info('%s log in from %s' % (_msg['name'], ip_port))

        cursor.execute("select * from user where name='%s'" % _msg['name'])
        user_info = cursor.fetchone()
        cursor.execute("select name, score from user order by score desc")
        rank = cursor.fetchall()[:5]

        global player_info
        global tables
        init_player_list = [_msg['name']]
        for item in player_info.values():
            init_player_list.append(item[0])
        init_table_list = []
        for i in range(16):
            for j in range(2):
                if tables[i][j]:
                    init_table_list.append(i*100+j)

        player_info[who] = [_msg['name'], State.IN_ROOM, ip_port]

        msg = {
            'cid' : 1000,
            'total_players': len(player_info),
            'player_list': init_player_list,
            'table_list': init_table_list,
            'user_info': user_info,
            'rank': rank
        }
        self.server.send_to_single(msg, who)

        msg = {
            'cid': 1001,
            'total_players': len(player_info),
            'ip': ip_port,
            'name': _msg['name']
        }
        self.server.send_to_all(msg, exclude=who)
        if not user_info:
            cursor.execute("insert into user(name) values('%s')" % _msg['name'])
            db.commit()

    def handle_logout(self, _msg, who):
        global player_info
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        logging.info('%s log out from %s' % (player_info[who][0], ip_port))

        msg = {
            'cid': 1002,
            'ip': ip_port,
            'total_players': len(player_info) - 1,
            'name': player_info[who][0]
        }
        self.server.send_to_all(msg, exclude=who)
        player_info.pop(who)
        self.server.inputs.remove(who)
        self.server.outputs.remove(who)
        self.server.message_queue.pop(who)

###########################################################
# 负责用户玩游戏的服务sid=2001
# cid=1001：用户选择桌子坐下
# cid=1002：用户离开桌子
# cid=1003：准备
# cid=1004：落子消息
###########################################################
class PlayService(Service):
    SERVICE_ID = 2001

    def __init__(self, ser):
        super(PlayService, self).__init__(PlayService.SERVICE_ID, ser)
        commands = {
            1001: self.handle_enter_table,
            1002: self.handle_leave_table,
            1003: self.handle_prepare,
            1004: self.handle_play,
            1005: self.handle_regret
        }
        self.registers(commands)

    def handle_enter_table(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        logging.info('%s enter table %d, side %d' % (ip_port, table/100, table%100))

        global tables
        tables[table/100][table%100] = who
        global player_info
        player_info[who][1] = State.IN_TABLE

        msg = {
            'cid': 1005,
            'table': table,
            'name': player_info[who][0],
            'ip': player_info[who][2]
        }
        #who.send(json.dumps(msg))
        #self.server.send_to_single(msg, who)
        self.server.send_to_all(msg, exclude=who)

        opponent = tables[table/100][1-table%100]
        if opponent:
            msg = {
                'cid': 10051,
                'has_opponent': 1,
                'name': player_info[opponent][0],
                'state': player_info[opponent][1],
                'ip': player_info[opponent][2]
            }
            self.server.send_to_single(msg, who)
        else:
            msg = {
                'cid': 10051,
                'has_opponent': 0
            }
            self.server.send_to_single(msg, who)


    def handle_leave_table(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        logging.info('%s leave table %d, side %d' % (ip_port, table/100, table%100))
        #TODO:游戏中离开判断
        global player_info
        player_info[who][1] = State.IN_ROOM
        global tables
        tables[table/100][table%100] = 0
        msg = {
            'cid': 1006,
            'table': table
        }
        #who.send(json.dumps(msg))
        #self.server.send_to_single(msg, who)
        self.server.send_to_all(msg, exclude=who)

    def handle_play(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        x = _msg['pos'][0]
        y = _msg['pos'][1]

        logging.info('%s put a chess on (%d, %d)' % (ip_port, x, y))

        opponent = tables[table/100][1-table%100]
        msg = {
            'cid': 1009,
            'pos': [x, y],
            'win': _msg['win']
        }
        self.server.send_to_single(msg, opponent)
        if _msg['win']:
            logging.info('%s win the game' % player_info[who][0])
            player_info[who][1] = State.IN_TABLE
            player_info[opponent][1] = State.IN_TABLE
            cursor.execute("select win, score from user where name='%s'" % player_info[who][0])
            info = cursor.fetchone()
            cursor.execute("update user set win=%d, score=%d where name='%s'" % (info[0]+1, info[1]+100, player_info[who][0]))

            cursor.execute("select lose, score from user where name='%s'" % player_info[opponent][0])
            info = cursor.fetchone()
            cursor.execute("update user set lose=%d, score=%d where name='%s'" % (info[0]+1, info[1]-100, player_info[opponent][0]))
            db.commit()
            # name = player_info[who][0]
            # cursor.execute("update user set win= where name=")

    def handle_prepare(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        logging.info('%s has prepared' % ip_port)
        global player_info
        player_info[who][1] = State.PREPARED
        global tables
        opponent = tables[table/100][1-table%100]

        if opponent:
            if player_info[opponent][1] == State.PREPARED:
                #对手也准备了，开始游戏
                msg = {
                    'cid' : 1007
                }
                self.server.send_to_single(msg, opponent)
                self.server.send_to_single(msg, who)
            else:
                msg = {
                    'cid' : 1008
                }
                self.server.send_to_single(msg, opponent)

    def handle_regret(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        ask_reply = _msg['type']
        opponent = tables[table/100][1-table%100]
        if ask_reply == 0:
            msg = {
                'cid': 1010,
                'type': 0
            }
            self.server.send_to_single(msg, opponent)
            logging.info('%s want to regret' % ip_port)
        else:
            msg = {
                'cid': 1010,
                'type': 1,
                'agree': _msg['agree']
            }
            self.server.send_to_single(msg, opponent)
            logging.info('opponent reply the regret with result %d' %_msg['agree'])


###########################################################
# 负责用户聊天的服务sid=2002
# cid=1001：用户大厅信息
# cid=1002: 用户桌子（房间）聊天
###########################################################
class ChatService(Service):
    SERVICE_ID = 2002

    def __init__(self, ser):
        super(ChatService, self).__init__(ChatService.SERVICE_ID, ser)
        commands = {
            1001: self.handle_room_chat,
            1002: self.handle_table_chat
        }
        self.registers(commands)

    def handle_room_chat(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        logging.info('%s room chat' % ip_port)
        global player_info
        msg = {
            'cid': 1003,
            'who': player_info[who][0],
            'content': _msg['content']
        }

        self.server.send_to_all(msg, exclude=who)

    def handle_table_chat(self, _msg, who):
        ip_port = who.getpeername()[0] + ':' + str(who.getpeername()[1])
        table = _msg['table']
        logging.info('%s table chat' % ip_port)
        global player_info
        global tables
        msg = {
            'cid': 1004,
            'who': player_info[who][0],
            'content': _msg['content']
        }
        opponent = tables[table/100][1-table%100]
        if opponent:
            self.server.send_to_single(msg, opponent)

###########################################################
# 消息分发器
###########################################################
class Dispatcher(object):
    def __init__(self):
        self.__service_map = {}

    def dispatch(self, msg, sender):
        sid = msg['sid']
        if not sid in self.__service_map:
            logging.error('bad service %d' % sid)
        svc = self.__service_map[sid]
        svc.handle(msg, sender)

    def register(self, sid, svc):
        self.__service_map[sid] = svc


class Server(object):
    def __init__(self, ip, port):
        self.dpt = Dispatcher()
        self.dpt.register(LoginService.SERVICE_ID, LoginService(self))
        self.dpt.register(PlayService.SERVICE_ID, PlayService(self))
        self.dpt.register(ChatService.SERVICE_ID, ChatService(self))

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((ip, port))
        self.sock.listen(30)

        self.inputs = [self.sock]
        self.outputs = []
        self.message_queue = {}

    def send_to_all(self, msg, exclude=None):
        for client in self.inputs:
            if client is not self.sock and client is not exclude:
                self.message_queue[client].put(msg)

    def send_to_single(self, msg, target):
        self.message_queue[target].put(msg)

    def serve_forever(self):
        while self.inputs:
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs, 20)
            for s in readable:
                if s is self.sock:
                    connection, address = s.accept()
                    connection.setblocking(False)
                    if connection not in self.inputs:
                        self.inputs.append(connection)
                    if connection not in self.outputs:
                        self.outputs.append(connection)
                    self.message_queue[connection] = Queue.Queue()
                else:
                    try:
                        msg = s.recv(1024)
                        self.dpt.dispatch(json.loads(msg), s)
                    except:
                        continue

            for s in writable:
                try:
                    msg = self.message_queue[s].get_nowait()
                except Queue.Empty:
                    pass
                except KeyError:
                    pass
                else:
                    try:
                        s.send(json.dumps(msg))
                    except:
                        logging.warning('abnormal exit')
                        self.inputs.remove(s)
                        self.outputs.remove(s)
                        self.message_queue.pop(s)
                        player_info.pop(s)
                        for i in range(16):
                            for j in range(2):
                                if tables[i][j] is s:
                                    tables[i][j] = 0
                                    break
                        s.close()

            for s in exceptional:
                logging.warning('exception connection %s' % s.getpeername())
                logging.warning('closing %s' % address)
                #stop listening for input on the connection
                self.inputs.remove(s)
                self.outputs.remove(s)
                self.message_queue.pop(s)
                player_info.pop(s)
                for i in range(16):
                    for j in range(2):
                        if tables[i][j] is s:
                            tables[i][j] = 0
                            break
                s.close()









