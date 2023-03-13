# UDPclient.py
from socket import * 
import sys
from html.parser import HTMLParser




class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.image_urls = []

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
            return fileContents
        fileContents +=recMessage.decode()

def getIMG(clientSocket):
    recMessage, serverAddress = clientSocket.recvfrom(2048)
    if (recMessage.decode() != "FILE NOT FOUND"):
        print("IMAGE RECEIVED")
    else:
        print(recMessage.decode())



if __name__ == '__main__':
    # if (len(sys.argv) != 4):
    #     print('Usage: python client.py server_ip server_port get_text_file')
    #     sys.exit()
    # serverName = sys.argv[1]
    # serverPort = int(sys.argv[2])
    # fileName = sys.argv[3]

    serverName = '127.0.0.1'
    serverPort = 12000
    fileName = "index.html"
    

    # Create UDP socket for server
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Attach server name, port to message; send into socket
    clientSocket.sendto(fileName.encode(), (serverName, serverPort))

    # Retrieves all of the html file from server
    HTMLFILE = getHTML(clientSocket)

    #Creating Parser and giving it the html file
    parser = MyHTMLParser()
    parser.feed(HTMLFILE)


    



    clientSocket.close()
