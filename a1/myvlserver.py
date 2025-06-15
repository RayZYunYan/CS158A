from socket import *


serverPort = 12000 #Server will listen on this port
BUFSIZE = 64 #Buffer size for recv(), following the requirements

def recv_all(sock, total_bytes):
    # Initialize an empty bytes object to accumulate received data
    data = b''
    # Keep receiving data until have the expected numnber of bytes
    while len(data) < total_bytes:
        # Receive the smaller of BUFSIZE or remaining bytes needed
        chunk = sock.recv(min(BUFSIZE, total_bytes - len(data)))
        # If recv returns empty, the connection was closed unexpectedly
        if not chunk:
            break
        # Append the received chunk to the total data
        data += chunk
    # Return the accumulated data
    return data

# Create a TCP socket and start listening
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("Server is ready")

while True:
    connectionSocket, addr = serverSocket.accept()
    print(f"Connected from {addr[0]}")

    # Read the first 2 bytes as the massage length
    len_bytes = recv_all(connectionSocket, 2)
    if not len_bytes:
        print("Connection closed before read length")
        connectionSocket.close()
        continue
    msg_len = int(len_bytes.decode())
    print(f"The message length is:{msg_len}")

    # Read the body of the message of fixed length
    sentence =  recv_all(connectionSocket, msg_len).decode()
    print(f"Processed message: {sentence}")

    # Convert to uppercase and send back
    capSentence = sentence.upper().encode()
    connectionSocket.sendall(len_bytes + capSentence)
    print(f"The length of message sent back: {msg_len}")
    print("Connection closed")
    connectionSocket.close()