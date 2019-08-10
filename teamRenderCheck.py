import c4d
import socket
from c4d import gui
import os
#Welcome to the world of Python


def main():
    minMax= [2,71]
    ip = []
    for i in range(minMax[0],minMax[1]+1):
        try:
            print 'schimpanse'+ str(i)
            ip.append(socket.gethostbyname('schimpanse'+ str(i)))
            
            
        except:
            print 'schimpanse'+ str(i), "is down"
    for i in ip:
        c4d.modules.net.NetRenderService.AddMachine([i+":5401","12345",True])

if __name__=='__main__':
    main()
