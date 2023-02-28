# UDPserver
from socket import *
import sys

if (len(sys.argv) != 3):
    print('Usage: python server.py server_port path_to_html ')
    sys.exit()
serverPort = int(sys.argv[1])
filename = sys.argv[2]


print(serverPort)
# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind socket to local port number 12000
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# Loop forever
while 1:
    # Read from UDP socket into message, getting client's
    # address (client IP and port)
    name, clientAddress = serverSocket.recvfrom(2048) 
    modifiedMessage = "Hello " + name.decode()+"!"

    # send string back to this client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    
