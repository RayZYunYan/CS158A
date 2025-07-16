# CS158A Assignment 4 - Leader Election

## 📌 Overview

This project implements an asynchronous ring-based Leader Election algorithm using Python socket programming with threading. Each process (node) connects to its neighbors in a unidirectional ring and participates in a UUID-based election to determine the leader.

This version improves upon the earlier `a3` project version with the following upgrades:
- Removed redundant locking mechanisms, simplifying the overall structure.
- Added silent and patient connection logic, allowing nodes to wait for outgoing connections instead of failing.
- Improved message sending reliability, ensuring no messages are lost during initial connection setup.
- Cleaned up logging, reducing repeated `Leader is decided` entries and maintaining a single decisive log.
- Removed unused functions and redundant code blocks, making the code cleaner and more aligned with course practices.

---

## 📂 Files

myleprocess.py       # Main Python program  
config.txt           # Two-line configuration file per node  
log1.txt             # Sample log for node 1  
log2.txt             # Sample log for node 2  
log3.txt             # Sample log for node 3  
README.md            # Instruction file

---

## ⚙️ How to Run

Prepare three configurations:

### config1.txt
127.0.0.1,5001  
127.0.0.1,5002

### config2.txt
127.0.0.1,5002  
127.0.0.1,5003

### config3.txt
127.0.0.1,5003  
127.0.0.1,5001

Start each node in separate terminals:

# Terminal 1
copy config1.txt config.txt  
python myleprocess.py log1.txt

# Terminal 2
copy config2.txt config.txt  
python myleprocess.py log2.txt

# Terminal 3
copy config3.txt config.txt  
python myleprocess.py log3.txt

You can start nodes at different times. Each node will wait until the outgoing connection is successful.

---

## ✅ Example Output

Server listening at ('127.0.0.1', 5001)  
Accepted connection from ('127.0.0.1', 5003)  
Outgoing connection established.  
Sent: uuid=0fd0..., flag=0  
Received: uuid=a98f..., flag=0, greater, 0  
Sent: uuid=a98f..., flag=0  
Received: uuid=a98f..., flag=1, greater, 1 (Leader=a98f...)  
Leader is decided to a98f...  
Election complete. Exiting.

---

## 📌 Notes

- This version is suitable for both synchronous and asynchronous node startup.
- Final logs are clean and leader decisions are logged once.
- Uses only `socket`, `threading`, `uuid`, `json` from standard Python libraries.
- No message loss during startup due to blocking connection setup.
- Resolves all the known instability issues from `a3` and simplifies the overall code.

---

## ✍️ Author
Ray Zhang
San Jose State University  
CS158A Summer 2025
