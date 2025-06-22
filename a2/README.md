```markdown
# CS158A - Assignment 2: Chat Server with Multiple Clients

## Overview

This assignment implements a TCP-based chat server that supports multiple concurrent clients. Each client can send raw text messages and receive messages from others. The server maintains a list of active client connections and relays each message to all other connected clients (excluding the sender).

Messages follow the format:
<client_port>: <message>

## Files

- mychatserver.py — the server-side script that handles client connections and message relaying  
- mychatclient.py — the client-side script that sends and receives messages from the server  
- README.md — this file

## How to Run

### 1. Start the Server

In a terminal, run:

    python mychatserver.py

Sample output:

    Server listening on 10.0.0.99:12345
    New connection from ('10.0.0.99', 51044)
    New connection from ('10.0.0.99', 51045)

Note: the IP address will reflect your machine's local network IP.

### 2. Start One or More Clients

In other terminals (or machines on the same network), run:

    python mychatclient.py

Sample output:

    Connected to chat server. Type 'exit' to leave.

## Example Output

### Server Terminal

    Server listening on 10.0.0.99:12345
    New connection from ('10.0.0.99', 51044)
    New connection from ('10.0.0.99', 51045)
    51044: Hi!
    51045: Hello!
    51045: How are you guys doing?
    Client ('10.0.0.99', 51045) disconnected.

### Client 1

    Connected to chat server. Type 'exit' to leave.

    51045: Hello!
    Hi!
    exit
    Disconnected from chat server

### Client 2

    Connected to chat server. Type 'exit' to leave.

    51044: Hi!
    How are you guys doing?
    exit
    Disconnected from chat server

## Features & Notes

- Uses TCP sockets (AF_INET, SOCK_STREAM)
- Buffer size for recv/send is fixed at 1024 bytes
- Server handles each client with a dedicated thread (via threading.Thread)
- Server continues accepting new connections until manually terminated (Ctrl + C)
- Client supports simultaneous input and message reception via threading
- Server relays messages using the required format f"{port_number}: {message}"
- Clients are removed from the active list upon sending "exit"


## Author

Ray Zhang  
San Jose State University  
CS158A Summer 2025
```
