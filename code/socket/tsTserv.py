# -*- coding:utf-8 -*-

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
    print("等待连接中......")
    tcpCliSock, addr = tcpServSock.accept()
    print "连接来自：", addr
    while True:
        data = tcpCliSock.recv(BUFSIZ).decode('utf-8')
        if not data:
            break
        time = ctime()
        msg = "[" + time +"]  "+ data

        tcpCliSock.send(msg.encode('utf-8'))
    tcpCliSock.close()

tcpServSock.close()
