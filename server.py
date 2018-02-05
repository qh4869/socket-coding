#!/usr/bin/env python3

import socket 
import readline
import select
import sys
from time import ctime

endallflag = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
select_input = [s, sys.stdin]
host = '124.16.71.153'
port = 9999
s.bind((host, port))
#print(s)
s.listen(5)
print('server start at {0}:{1}'.format(host, port))
while endallflag:
    print('wait for connection...') 
    conn, addr = s.accept()
    select_input.append(conn) 
    endflag = 1
    print ('Connected by {0}'.format(addr))
    while endflag:
        readyInput, readyOutput, readyException = \
                select.select(select_input,[],[])
        for indata in readyInput:
            if indata == conn: #接收信息
                data_rec = conn.recv(1024).decode()
                if data_rec == 'end!':
                    conn.close()
                    print('The client {0} has disconnected'.format(addr))
                    endflag = 0
                elif data_rec == 'end_all!':
                    conn.close()
                    print('The client {0} has disconnected'.format(addr))
                    endflag = 0
                    s.close()
                    print('The server at {0}:{1} has closed'.format(host, port))
                    endallflag = 0
                else:
                    print('[{0}] '.format(ctime())+data_rec)
            elif indata == sys.stdin: #发送信息
                data_send = sys.stdin.readline().strip('\n')
                conn.send(data_send.encode())
