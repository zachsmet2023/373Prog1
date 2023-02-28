# UDPserver
from socket import *
import sys

if (len(sys.argv) != 3):
    print('Usage: python ProjectClient.py server_port file_name')
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

    # send upper case string back to this client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)

    toOutput = []

    file = open(filename, 'r')
    for i in file:
        j = i.split()
        for m in range(len(j)):
            if j[m][0] == '%':
                # here is where we ask the client for input
                madMessage = j[m].replace('%', '', 1)
                serverSocket.sendto(madMessage.encode(), clientAddress)
                madResponse, clientAddress = serverSocket.recvfrom(2048)
                toOutput.append(madResponse.decode())
            else:
                toOutput.append(j[m])
    file.close()
    urdone = '$h!tH3@d'
    serverSocket.sendto(urdone.encode(), clientAddress)

    for i in range(len(toOutput)):
        storytime = toOutput[i]+' '
        serverSocket.sendto(storytime.encode(), clientAddress)
    urdone = 'Big Chungus'
    serverSocket.sendto(urdone.encode(), clientAddress)
