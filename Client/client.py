# UDPclient.py
from socket import *  # include Python's socket library
import sys

if (len(sys.argv) != 4):
    print('Usage: python ProjectClient.py server_ip server_port file_name')
    sys.exit()
serverName = sys.argv[1]
serverPort = int(sys.argv[2])
fileName = sys.argv[3]

# Create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Get user keyboard input
message = input('What is your name?')

# Attach server name, port to message; send into socket
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Read reply characters from socket into string
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Print out received string and close socket
print(modifiedMessage.decode())


# Attach server name, port to message; send into socket

while 1:
    madMessage, serverAddress = clientSocket.recvfrom(2048)
    if madMessage.decode() == '$h!tH3@d':
        break
    madResponse = input(madMessage.decode()+' : ')
    clientSocket.sendto(madResponse.encode(), (serverName, serverPort))

myfile = open(fileName, 'w')
while 1:
    storyTime, serverAddress = clientSocket.recvfrom(2048)
    if storyTime.decode() == 'Big Chungus':
        break
    myfile.write(storyTime.decode())
clientSocket.close()
