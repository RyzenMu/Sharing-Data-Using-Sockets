import socket
mySock = socket.socket()
host = '192.168.1.142'
port = 65535 #reserve a port number
mySock.bind((host, port))
mySock.listen(1)
while True:
        conn, addr = mySock.accept()
        while True:
                data = conn.recv(1024)
                if data.decode() == 'EOF':
                        break
                conn.send(data + 'mila water')
        conn.close()

mySock.close()
