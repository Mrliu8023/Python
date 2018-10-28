# -*- coding:utf-8 -*-
"""
@author = xijue.
"""

from socket import *
from time import ctime

HOST = ''
PORT = 2000
BUFSIZ = 1024
ADDR = (HOST,PORT)

#创建套接字
tcpServSock = socket(AF_INET, SOCK_STREAM)
tcpServSock.bind(ADDR)
tcpServSock.listen(5)

while True:
    print("聊天室等待连接中......")
    tcpCliSock, addr = tcpServSock.accept()
    print "连接来自：", addr
    while True:
        try:
            datarecv = tcpCliSock.recv(BUFSIZ).decode('utf-8')
            if not datarecv:
                break
            print "[" + ctime() + "]"
            print "<<<"+datarecv
            msg = raw_input(">>>")
            msg = unicode(msg, 'utf-8')
            tcpCliSock.send(msg.encode('utf-8'))
        except Exception,e:
            print(e)
            break
    tcpCliSock.close()

tcpServSock.close()
