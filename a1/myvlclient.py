from socket import *

# Server settings
SERVER = 'localhost'  # Replace with server IP if not running locally
clientPort = 12000
BUFSIZE = 64  # Must match server-side buffer size


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
def main():
    user_input = input("Input lowercase sentence: ")
    print(f"{user_input}  # This is a user input. {user_input[:2]} is the number of characters in the following sentence. (n = 2)")


    # First 2 characters must be the length of the message body
    try:
        msg_len = int(user_input[:2])
        message = user_input[2:]
    except:
        print("Invalid input format. Use 2-digit length followed by message.")
        return

    # Check consistency
    if msg_len != len(message):
        print(f"Length mismatch: declared {msg_len}, actual {len(message)}")
        return

    # Prepare data to send: length + message
    full_msg = user_input.encode()

    # Create TCP socket and send the message
    with socket(AF_INET, SOCK_STREAM) as client_sock:
        client_sock.connect((SERVER, clientPort))
        client_sock.sendall(full_msg)

        # Receive 2-byte length prefix from server
        len_bytes = recv_all(client_sock, 2)
        if not len_bytes:
            print("Connection closed before length received")
            return

        response_len = int(len_bytes.decode())

        # Receive the uppercase message
        response = recv_all(client_sock, response_len).decode()

        # Print the result
        print("From Server:", response)

if __name__ == '__main__':
    main()
