# UDPclient.py
from socket import * 
import os
import sys
from html.parser import HTMLParser




class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()

    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for name, value in attrs:
                if name == "src":
                    clientSocket.sendto(value.encode(), (serverName, serverPort))
                    getIMG(clientSocket)

                   

def getHTML(clientSocket):
  fileContents = ""
  while 1:
        recMessage, serverAddress = clientSocket.recvfrom(2048)
        if (recMessage.decode() == "EOF"):
            print("HTML RECEIVED SUCCESSFULLY")
            return fileContents
        fileContents +=recMessage.decode()

def getIMG(clientSocket):
    recMessage, serverAddress = clientSocket.recvfrom(2048)
    if (recMessage.decode() != "FILE NOT FOUND"):
        print("IMAGE RECEIVED SUCCESSFULLY")
    else:
        print(recMessage.decode())



if __name__ == '__main__':
    # if (len(sys.argv) != 4):
    #     print('Usage: python client.py server_ip server_port get_text_file')
    #     sys.exit()
    # serverName = sys.argv[1]
    # serverPort = int(sys.argv[2])
    # filePath = sys.argv[3]

    serverName = 'compsci04.snc.edu'
    serverPort = 3900
    filePath = 'getTextFile.txt'
    

    # Create UDP socket for server
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # opens text doc, extracts GET message sends it to server
    if os.path.exists(filePath):
        with open(filePath, 'rb') as f:
            data = f.read()
        clientSocket.sendto(data, (serverName, serverPort))
    else:
        print("TXT PATH DOESNT EXIST") 

    # Retrieves all of the html file from server
    HTMLFILE = getHTML(clientSocket)

    #Creating Parser and giving it the html file
    parser = MyHTMLParser()
    print("~~~~STARTING PARSER~~~~")
    parser.feed(HTMLFILE)
    print("~~~~STOPPING PARSER~~~~")


    clientSocket.close()
