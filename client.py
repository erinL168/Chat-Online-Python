import socket

##socket is already a library included in python 3
##we are creating a socket object 
##socket(socket family type: AF_INIT corresponds to ipv4, type of socket: SOCK_STREAM [streaming socket tcp] )
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)