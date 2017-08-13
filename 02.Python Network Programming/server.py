
#Simple Server

import socket
host = '' #Bind to all interface
port = 8089

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)

print ("Server is running on port %d;press Ctrl-C to terminate.")

while 1:
    clientsock,clientaddr = s.accept()
    clientfile = clientsock.makefile('rw')
    #fd.write(filename.encode('utf-8') + "\r\n".encode('utf-8'))
    #clientfile.write("Welcome".encode('utf-8') + "\r\n".encode('utf-8'))
    clientfile.write("Welcome, " + str(clientaddr) + "\n")
    clientfile.write("Please enter a string:")
    line = clientfile.readline().strip()
    clientfile.write("You entered %d characters.\n" % len(line))
    clientfile.write("Welcome " + line + ".\n")
    clientfile.close()
    clientsock.close()



