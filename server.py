import socket
import time
import pickle



HEADERSIZE = 10

##socket is already a library included in python 3
##we are creating a socket object 
##socket(socket family type: AF_INIT corresponds to ipv4, type of socket: SOCK_STREAM [streaming socket tcp] )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# (socket.local host, port number)

s.bind((socket.gethostname(), 1236))
s.listen(5) #queue of 5, if messages start stacking up

while True: #we will listen forever for connections
    clientsocket, address = s.accept() 
    #anybody connects, then we store the client socket into
    #clientsocket and their address stored in address (s.accept() is basically another socket)
    print(f"Connection from {address} has been established!")


    d = {1: "hey", 2: "there"}
    msg = pickle.dumps(d)
    #print(msg)

    #convert to bytes (utf-8 bytes)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8") + msg

    #f string that is less than 20 appended with the message
    #you can append more brackets to more brackets
    # msg = f'{len(msg):<20}'+msg

    #this basically says the length of message and basically :< means string formatting is to the left, carrot is center ^
    #msg = f'{len(msg):<{HEADERSIZE}}' + msg

    clientsocket.send(bytes(msg, "utf-8"))

    while True:
        time.sleep(3)
        msg = f"The time is! {time.time()}"
        msg = f'{len(msg):<{HEADERSIZE}}'+msg
        clientsocket.send(bytes(msg, "utsf-8"))



