from socket import *
import threading

# Server config
serverName = 'localhost' # Replace with actual server IP
serverPort = 12345
BUFSIZE = 1024

# TCP client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print("Connected to chat server. Type 'exit' to leave.\n")

# Receive messages from the server
def receive():
    while True:
        try:
            data = clientSocket.recv(BUFSIZE)
            if not data: 
                break
            print(data.decode())
        except:
            break

# Start the receive thread
threading.Thread(target=receive, daemon=True).start()

# Main loop: read user input and send to server
try:
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        clientSocket.sendall(message.encode())
except KeyboardInterrupt:
    pass

# Dissconnect from the server
clientSocket.close()
print("Disconnected from chat server")