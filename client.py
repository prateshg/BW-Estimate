import socket
import sys
import time
import os
from socket import error as socket_error

host = sys.argv[1]
port = 12345
credit = 0                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MESSAGE=""
t =[]
for i in range(1458):
	MESSAGE=MESSAGE+"a"
MESSAGE=MESSAGE+ "0123456789"

for i in range(100):
	s.sendto(MESSAGE, (host, port))

s.close()
