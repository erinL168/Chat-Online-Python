import socket

##socket is already a library included in python 3
##we are creating a socket object 
##socket(socket family type: AF_INIT corresponds to ipv4, type of socket: SOCK_STREAM [streaming socket tcp] )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (socket.local host, port number)

s.bind((socket.gethostname(), 1234))
s.listen(5) #queue of 5, if messages start stacking up

while True: #we will listen forever for connections
    clientsocket, address = s.accept() 
    #anybody connects, then we store the client socket into
    #clientsocket and their address stored in address (s.accept() is basically another socket)
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    