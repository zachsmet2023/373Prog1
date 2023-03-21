# UDPserver
from socket import *
import sys
import os

# METHOD
def incomingMes(serverSocket, directoryPath):
    request, client_address = serverSocket.recvfrom(2048)
    request = request.decode()

    #if nothing 
    if not request:
        return
    
    #if the request is for the html file 
    if (request == "GET index.html"):
        filePath = os.path.join(directoryPath, "index.html")
        if os.path.exists(filePath):
            with open(filePath, 'rb') as f:
                data = f.read()

            #File is to big so need to chunk it up to send
            chunkSize = 1024
            for i in range(0, len(data), chunkSize):
                chunk = data[i:i+chunkSize]
                serverSocket.sendto(chunk, client_address)

            serverSocket.sendto(EOFMSG.encode(), client_address)
            
            print('HTML SENT SUCCESSFULLY')
        else:
            serverSocket.sendto(ERRORMSG.encode(), client_address)

    #if the request is the end of transmission message
    elif (request == "SHITHEAD"):
        serverSocket.close()
        
    #if the request is for an image
    else:
        response = os.path.join(directoryPath, request)
        if os.path.exists(response):
            serverSocket.sendto(response.encode(), client_address)
            print("IMAGE SENT SUCCESSFULLY")
        else:
            serverSocket.sendto(ERRORMSG.encode(), client_address)



if __name__ == '__main__':

    ERRORMSG = "FILE NOT FOUND"
    EOFMSG = "EOF"

    # if (len(sys.argv) != 3):
    #     print('Usage: python3 server.py server_port path_to_html ')
    #     sys.exit()
    #serverPort = int(sys.argv[1])
    #filePath = sys.argv[2]
    directoryPath = "SampleWebPage/"
    serverPort = 12000
    


    # Create UDP socket
    serverSocket = socket(AF_INET, SOCK_DGRAM)

    # Bind socket to local port number 12000
    serverSocket.bind(('', serverPort))
    print("The server is ready to receive")


    while 1:
       incomingMes(serverSocket, directoryPath)

    
