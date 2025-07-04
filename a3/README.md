# CS158A Assignment 3 - Leader Election

## 📌 Overview

This project implements an asynchronous ring-based Leader Election algorithm using basic socket and threading programming in Python. Each process (node) communicates with its two neighbors over TCP connections and participates in the election using UUID-based identity.

---

## 📂 Files

myleprocess.py       # Main program file  
config.txt           # Example configuration for one node  
log1.txt             # Log from node 1  
log2.txt             # Log from node 2  
log3.txt             # Log from node 3

---

## ⚙️ How It Works

- Each node:
  - Creates a unique UUID as its identity.
  - Connects to the next node (client) and accepts connection from the previous node (server).
  - Sends its UUID once and participates in the election.
- The node with the highest UUID becomes the leader.
- Once a node determines it is the leader, it broadcasts a termination message (flag=1) around the ring.
- Each node writes a log when sending or receiving a message.

---

## 🧪 How to Run Locally (3 processes on same machine)

Use 127.0.0.1 and different ports. Prepare three configurations:

### config1.txt
127.0.0.1,5001  
127.0.0.1,5002

### config2.txt
127.0.0.1,5002  
127.0.0.1,5003

### config3.txt
127.0.0.1,5003  
127.0.0.1,5001

Then in three terminals, run:

# Terminal 1
copy config1.txt config.txt  
python myleprocess.py log1.txt

# Terminal 2
copy config2.txt config.txt  
python myleprocess.py log2.txt

# Terminal 3
copy config3.txt config.txt  
python myleprocess.py log3.txt

---

## ✅ Example Output (from logX.txt)

Sent: uuid=9d5e..., flag=0  
Received: uuid=a85f..., flag=0, greater, 0  
Ignored  
Received: uuid=9d5e..., flag=0, same, 0  
Leader is decided to 9d5e...  
Sent: uuid=9d5e..., flag=1  
Received: uuid=9d5e..., flag=1, same, 1 (Leader=9d5e...)

---

## 📌 Notes

- Only one config.txt is submitted, but the three logs were generated using three different configs.
- This program uses only basic socket + threading, no third-party libraries.
- Designed to match the style of CS158A lecture slides.

---


## ✍️ Author

Ray Zhang  
San Jose State University  
CS158A Summer 2025
