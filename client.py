#! /usr/bin/env python3


import socket
import readline #如果不import这个模块，input中文backspace之后的显示会不正确（不知道为啥）
#这个模块的原来目的就是input输入自动补全和记录历时输入

endflag = 1;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
#s.bind(('124.16.71.203', 9998))
host = '124.16.71.203'
port = 9999
s.connect((host, port))
try:
    while endflag:
            cmd = input('Please input msg:')
            if cmd == 'end!' or cmd == 'end_all!':
                    s.send(cmd.encode())
                    s.close()
                    endflag = 0
            else:
                    s.send(cmd.encode())
                    data = s.recv(1024)
                    print(data.decode())
except ConnectionRefusedError:
    print('Fail to Connect!')
