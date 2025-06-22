# CS158A Assignment 2: Chat Server with Multiple Clients

This project implements a TCP-based multi-client chat system. A central server relays messages between all connected clients. Clients can send messages at any time, receive messages from others, and disconnect using the `exit` command.

## 🔧 Files

- `mychatserver.py` — The TCP server that accepts clients and broadcasts messages.
- `mychatclient.py` — The TCP client that connects to the server and sends/receives chat messages.
- `README.md` — This file.

## 💬 Message Format

Each message sent from a client is raw user input.  
The server relays the message to all other clients in the format:

```text
<client_port>: <message>
```

Example:
```text
51044: Hello everyone!
```

## 🖥 How to Run

### Start the Server

Open a terminal and run:

```text
python mychatserver.py
```

You should see:

```text
Server listening on 10.0.0.99:12345
New connection from ('10.0.0.99', 51044)
```

> Note: the IP address will vary depending on your local network.

### Start One or More Clients

Open additional terminals or devices and run:

```text
python mychatclient.py
```

You will see:

```text
Connected to chat server. Type 'exit' to leave.
```

## 🧪 Example Output

### Server Terminal

```text
Server listening on 10.0.0.99:12345
New connection from ('10.0.0.99', 51044)
New connection from ('10.0.0.99', 51045)
51044: Hi!
51045: Hello!
51045: How are you guys doing?
Client ('10.0.0.99', 51045) disconnected.
```

### Client 1

```text
Connected to chat server. Type 'exit' to leave.

51045: Hello!
Hi!
exit
Disconnected from chat server
```

### Client 2

```text
Connected to chat server. Type 'exit' to leave.

51044: Hi!
How are you guys doing?
exit
Disconnected from chat server
```

## ✅ Requirements Met

- ✅ TCP sockets (AF_INET, SOCK_STREAM)
- ✅ Buffer size for recv/send is 1024 bytes
- ✅ Multi-threaded server: each client handled by a separate thread
- ✅ Server maintains active client list
- ✅ Messages broadcasted to all clients except sender
- ✅ Format: `<port_number>: <message>`
- ✅ "exit" input removes client from server and closes socket
- ✅ Server runs until manually terminated
- ✅ Client supports concurrent send and receive

## 🧪 Testing

Tested on both single-machine (localhost) and local network IP configurations:

```text
Server listening on 10.0.0.99:12345
New connection from ('10.0.0.99', 51792)
51044: Hello!
```

```text
Connected to chat server. Type 'exit' to leave.
51044: Hello!
exit
Disconnected from chat server
```

## ✍️ Author

Ray Zhang  
San Jose State University  
CS158A Summer 2025

