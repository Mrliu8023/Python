# -*- coding:utf-8 -*-
"""
@author = xijue
"""

from socket import *
from time import ctime
import threading

flag = 0

def send(sock, none):
    while True:
        msg = raw_input("<<")
        if not msg:
            break
        msg = unicode(msg, 'utf-8')
        sock.send(msg.encode('utf-8'))
    sock.close()
    global flag
    flag = 1

def recv(sock, BUFSIZ):
    global flag
    while True:
        try:
            data = sock.recv(BUFSIZ).decode('utf-8')
            if not data:
                break
            print '\n>>'
            print "[" + ctime() + "]    "+data
            print '<<',
        except Exception,e:
            break
    sock.close()
    flag = 1

def main():
    global flag
    HOST = ''
    PORT = 2000
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    # 创建套接字
    tcpServSock = socket(AF_INET, SOCK_STREAM)
    tcpServSock.bind(ADDR)
    tcpServSock.listen(5)
    while True:
        print("聊天室等待连接中......")
        tcpCliSock, addr = tcpServSock.accept()
        print "连接来自：", addr
        try:
            #创建收发线程
            recvmsg = threading.Thread(target = recv, args = (tcpCliSock, BUFSIZ))
            sendmsg = threading.Thread(target = send, args = (tcpCliSock, None))
            recvmsg.start()
            sendmsg.start()

            recvmsg.join()
            sendmsg.join()

        except Exception,e:
            print(e)
            break

if __name__ == '__main__':
    main()