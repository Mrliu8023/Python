# -*- coding:utf-8 -*-
"""
@author = xijue
"""

from socket import *
from time import ctime

HOST = ''
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpServSock = socket(AF_INET, SOCK_DGRAM)
udpServSock.bind(ADDR)

while True:
    #data：客户端发送的数据，addr：客户端的地址
    print("等待消息......")
    data, addr = udpServSock.recvfrom(BUFSIZ)
    if not data:
        break
    time = ctime()
    #接收有中文的数据时，需要先解码
    data = u"[" + time + "]   " + data.decode('utf-8')
    udpServSock.sendto(data.encode('utf-8'), addr)
    print "收到来自:", addr,"的数据并且返回加了时间戳的数据"

udpServSock.close()

