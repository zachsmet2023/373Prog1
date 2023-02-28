# UDPclient.py
from socket import *  # include Python's socket library
import sys

if (len(sys.argv) != 4):
    print('Usage: python client.py server_ip server_port get_text_file')
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



clientSocket.close()
