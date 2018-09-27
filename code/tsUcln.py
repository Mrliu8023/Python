# -*- coding:utf-8 -*-
"""
@author = xijue
"""

from socket import *

#
HOST = '192.168.161.1'
PORT = 8080
BUFSIZ = 1024
ADDR = (HOST, PORT)

udpCliSock = socket(AF_INET, SOCK_DGRAM)

while True:
    data = raw_input("请输入您要发送的数据:")
    if not data:
        break
    data = unicode(data, 'utf-8')
    #发送的数据bytes，发送时需要编码
    udpCliSock.sendto(data.encode('utf-8'), ADDR)
    msg, addr = udpCliSock.recvfrom(BUFSIZ)
    if not msg:
        break
    print msg.decode('utf-8')
udpCliSock.close()