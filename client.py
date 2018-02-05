#! /usr/bin/env python3

import socket
import readline #如果不import这个模块，input中文backspace之后的显示会不正确（不知道为啥）
#这个模块的原来目的就是input输入自动补全和记录历时输入
import select
import sys
from time import ctime

endflag = 1;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
select_input = [s, sys.stdin]
host = '124.16.71.153'
port = 9999
try: 
    s.connect((host, port)) 
    while endflag:
        readyInput, readyOutput, readyException = \
                select.select(select_input,[],[]) 
        for indata in readyInput:
            if indata == s: #接受信息
                data_rec = s.recv(1024).decode()
                print('[{0}] '.format(ctime())+data_rec) 
            elif indata == sys.stdin: #发送信息
                data_send = sys.stdin.readline().strip('\n')
                if data_send == 'end!' or data_send == 'end_all!':
                    s.send(data_send.encode())
                    s.close()
                    endflag = 0
                else:
                    s.send(data_send.encode())
except ConnectionRefusedError:
    print('Fail to Connect!')
