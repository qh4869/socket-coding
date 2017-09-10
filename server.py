import socket 
endallflag = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#host = socket.gethostname()
host = '124.16.71.203'
port = 9999
s.bind((host, port))
#print(s)
s.listen(5)
print('server start at {0}:{1}'.format(host, port))
print('wait for connection...')
while endallflag:
	conn, addr = s.accept()
	endflag = 1
	print ('Connected by {0}'.format(addr))
	while endflag:
		data = conn.recv(1024).decode()
		if data == 'end!':
			conn.close()
			print('The client {0} has disconnected'.format(addr))
			endflag = 0
		elif data == 'end_all!':
			conn.close()
			print('The client {0} has disconnected'.format(addr))
			endflag = 0
			s.close()
			print('The server at {0}:{1} has closed'.format(host, port))
			endallflag = 0
		else:
			print(data)
			conn.send('server received your message'.encode())
