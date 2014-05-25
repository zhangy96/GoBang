# -*- coding: utf-8 -*-
__author__ = 'gzs2473'

from server.server import Server

if __name__ == '__main__':
    server = Server('127.0.0.1', 12345)
    server.serve_forever()


