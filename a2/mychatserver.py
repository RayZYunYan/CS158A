from socket import *
import threading

# Server config
serverPort = 12345
serverSocket = socket(AF_INET, SOCK_STREAM) # TCP socket
serverSocket.bind(('',serverPort))
serverSocket.listen()

hostName = gethostname()
localIP = gethostbyname(hostName)
print(f"Server listening on {localIP}:{serverPort}")

clientSockets = []
lock = threading.Lock()
BUFSIZE = 1024

def sendToAll(message: bytes, senderSocket: socket):
    with lock:
        for clientSocket in clientSockets:
            if clientSocket != senderSocket:
                try:
                    clientSocket.sendall(message)
                except:
                    clientSocket.close()
                    clientSockets.remove(clientSocket)

def handleClient(connectionSocket: socket, clientAddress):
    clientPort = clientAddress[1]

    # Add the new client to the list
    with lock:
        clientSockets.append(connectionSocket)
    
    try:
        while True:
            data = connectionSocket.recv(BUFSIZE)
            if not data:
                break
            message = data.decode().strip()

            # Disconnect if client sends "exit"
            if message.lower() == "exit":
                print(f"Client {clientAddress} disconnected.")
                break

            # Format and broadcast the message
            formatted = f"{clientPort}: {message}".encode()
            print(formatted.decode())
            sendToAll(formatted, connectionSocket)
    except:
        pass
    finally:
        # Remove the client from the list and close the socket
        with lock:
            if connectionSocket in clientSockets:
                clientSockets.remove(connectionSocket)
        connectionSocket.close()
        print(f"Client {clientAddress} disconnected.")

while True:
    try:
        connectionSocket, clientAddress = serverSocket.accept()
        print(f"New connection from {clientAddress}")
        threading.Thread(target=handleClient, args=(connectionSocket, clientAddress)).start()
    except KeyboardInterrupt:
        print("Server shutting down.")
        break

serverSocket.close()