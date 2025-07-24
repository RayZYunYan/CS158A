import socket
import ssl

# Target host and port
HOST = "www.google.com"
PORT = 443
REQUEST = f"GET / HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"

# Create a TCP socket
context = ssl.create_default_context()
with socket.create_connection((HOST, PORT)) as sock:
    # Wrap the socket with SSL
    with context.wrap_socket(sock, server_hostname=HOST) as ssock:
        print(f"[+] Connected to {HOST}:{PORT} with SSL")
        
        # Send the HTTP GET request
        ssock.sendall(REQUEST.encode())

        # Receive the full response
        response_data = b""
        while True:
            data = ssock.recv(4096)
            if not data:
                break
            response_data += data

# Split headers and body
try:
    header_end = response_data.find(b"\r\n\r\n")
    if header_end == -1:
        raise ValueError("Invalid HTTP response: no header-body separator found")
    
    body = response_data[header_end+4:]

    with open("response.html", "wb") as f:
        f.write(body)

    print("[+] HTML body saved to response.html")

except Exception as e:
    print("[-] Error processing response:", e)
