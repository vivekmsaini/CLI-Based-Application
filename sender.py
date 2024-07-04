import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 

target_ip = "192.168.110.166"
# target_ip = "127.0.0.1"
target_port = 2525

while True:
   message = input("plz enter message : ")
   message = message.encode("ascii")
   s.sendto(message,(target_ip,target_port))
   print("your message has been successfully sent!")