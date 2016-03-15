import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('www.pythonlearn.com', 80))
my_socket.send('GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

while True :
    data = my_socket.recv(512)
    if (len(data) < 1) : break
    print data
    
my_socket.close()
