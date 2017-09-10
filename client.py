import socket
endflag = 1;

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = '124.16.71.203'
port = 9999
s.connect((host, port))
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
