# -*- coding:utf-8 -*-
"""
@author = xijue
"""
import threading
from time import ctime
from socket import *

#收消息
def recv(sock, BUFSIZ):
    while True:
        data = sock.recv(BUFSIZ)
        if not data:
            break
        data.decode('utf-8')
        print "\n>>"
        print "["+ctime()+"]  " +data
        print '<<'

#发消息
def send(sock, none):
    while True:
            data = raw_input("<<")
            if not data:
                break
            data = unicode(data, 'utf-8')
            sock.send(data.encode('utf-8'))


def main():
    HOST = '192.168.161.1'
    PORT = 2000
    ADDR = (HOST, PORT)
    BUFSIZ = 1024

    #创建套接字
    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)

    #创建收发线程
    recvt = threading.Thread(target=recv, args=(tcpCliSock, BUFSIZ))
    sendt = threading.Thread(target=send, args=(tcpCliSock,None))

    recvt.start()
    sendt.start()

    recvt.join()
    recvt.join()
    tcpCliSock.close()

if __name__ == "__main__":

    main()