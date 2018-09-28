# -*- coding:utf-8 -*-
"""
@author = xijue
"""

from socket import *
from time import ctime

HOST = '127.0.0.1'
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpClnSock = socket(AF_INET, SOCK_STREAM)
try:
    tcpClnSock.connect(ADDR)
    print "已连接"+HOST
    while True:
        try:
            data = raw_input(">>>")
            #将输入的data转成utf-8编码，不然会报错：'ascii' codec can't decode byte 0xef in position 0:ordinal not in range(128)
            data = unicode(data, 'utf-8')
            if not data:
                break
            tcpClnSock.send(data.encode('utf-8'))
            data = tcpClnSock.recv(BUFSIZ).decode('utf-8')
            if not data:
                break
            print "[" + ctime() +  "]"
            print "<<<" + data
        except Exception,e:
            break
except Exception,e:
    print "连接失败"
tcpClnSock.close()

