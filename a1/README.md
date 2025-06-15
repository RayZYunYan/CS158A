# CS158A Assignment 1: Variable-Length Message Client/Server

This project implements a TCP-based client-server application that can send and receive variable-length messages using a 2-byte length prefix. The server returns the received message in all uppercase letters.

## 🔧 Files

- `myvlserver.py` — The TCP server that receives, processes, and returns uppercase messages.
- `myvlclient.py` — The TCP client that sends length-prefixed messages to the server.
- `README.md` — This file.

## 📜 Message Format

The message starts with a 2-character length field (n = 2), followed by the message body of that length.  
Example input:  
```
10helloworld
```
This means the message body is `helloworld` (10 characters).

## 🖥 How to Run

### Start the Server
Open a terminal and run:
```text
python myvlserver.py
```

You should see:
```text
Server is ready
```

### Run the Client
Open another terminal and run:
```text
python myvlclient.py
```

You will be prompted to input a message:
```text
Input lowercase sentence: 10helloworld
10helloworld  # This is a user input. 10 is the number of characters in the following sentence. (n = 2)
From Server: HELLOWORLD
```

### Server Output
```text
Connected from 127.0.0.1 (Varies depending on server settings)
The message length is: 10
Processed message: helloworld
The length of message sent back: 10
Connection closed
```

## ✅ Requirements Met

- ✅ TCP sockets (not UDP)
- ✅ Fixed `recv()` buffer size of 64 bytes
- ✅ Variable-length message with 2-byte length prefix
- ✅ Server prints message info and returns uppercase response
- ✅ Client terminates after receiving full response
- ✅ Server runs continuously until manually terminated
- ✅ Graceful handling of input format and length mismatches
- ✅ All messages use UTF-8 characters between U+0000 and U+007F

## 🧪 Testing

Tested successfully by running both server and client on the same machine using:
```text
SERVER = '127.0.0.1'
```

With sample inputs like:
```text
03cat
10helloworld
08sentence
```

All responses were received correctly and converted to uppercase.

## ✍️ Author

Ray Zhang  
San Jose State University  
CS158A Summer 2025
