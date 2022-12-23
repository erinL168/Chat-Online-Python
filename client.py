import socket
import pickle
HEADERSIZE = 10


##socket is already a library included in python 3
##we are creating a socket object 
##socket(socket family type: AF_INIT corresponds to ipv4, type of socket: SOCK_STREAM [streaming socket tcp] )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1236))

#connects to port 1234

msg = s.recv(1024) # this is our buffer size
#we can send anything under 24 bytes
#why do we need to buffer data, because if we 
full_msg = "hello"
while True:
    full_msg = b'' #bytes msg?
    new_msg = True
    while True:
        
        msg = s.recv(16)
        if new_msg:
            print(f"new message length:" {msg[:HEADERSIZE]}) # length of message
            msglen = int(msg[:HEADERSIZE]) #python will allow this (you'd need .strip to get rid of the extra spaces)
            new_msg = False #not longer than max

        
        print(f"full message length: {msglen}")
        #every loop appends to new msg
        full_msg += msg

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)


            new_msg = True
            full_msg = b"" #emptied out we can continue if new messages

        # full_msg += msg.decode("utf-8")
        
    print(full_msg)   
    
#a byte stream, recieved as bytes, sent as bytes, so all we did is decode it
