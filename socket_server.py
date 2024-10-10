import socket

host= "172.27.46.67"

port=50003

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((host,port))

message=input(">> ")

while message.lower().strip()!="quit":
    if(message!=""):
        client_socket.send(message.encode())
        data=client_socket.recv(1024)
        print("response from server : "+str(data))
    message = input(">> ")
client_socket.close()