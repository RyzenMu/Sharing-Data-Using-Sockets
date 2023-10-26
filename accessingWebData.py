import socket

mySock = socket.socket()
host = 'marvin.cs.uidaho.edu'
port = 80 # HTTP host
mySock.connect((host, port))
mySock.send('GET http://marvin.cs.uidaho.edu/Teaching/CS515/pythonTutorial.pdf HTTP/1.0 \n\n'.encode())
fp = open('pythonGuidoVanRossum.pdf', 'wb')
while True:
        data = mySock.recv(512)
        if (len(data)<1):
                break
        fp.write(data)

fp.close()
mySock.close()
