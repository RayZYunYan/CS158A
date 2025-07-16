from socket import *
import threading
import uuid
import json
import time
import sys

# Configuration file and log file paths
CONFIG_FILE = "config.txt"
LOG_FILE = None

class Message:
    def __init__(self, uuid_val, flag):
        self.uuid = uuid_val
        self.flag = flag

    # Serialize message to JSON string
    def to_json(self):
        return json.dumps({"uuid": str(self.uuid), "flag": self.flag})

    # Deserialize message from JSON string
    @staticmethod
    def from_json(s):
        data = json.loads(s)
        return Message(uuid.UUID(data["uuid"]), data["flag"])

def write_log(line):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")
    print(line)

def load_config():
    with open(CONFIG_FILE, "r") as f:
        lines = f.read().splitlines()
        server_ip, server_port = lines[0].split(",")
        client_ip, client_port = lines[1].split(",")
        return (server_ip.strip(), int(server_port.strip())), (client_ip.strip(), int(client_port.strip()))

class ElectionNode:
    def __init__(self, log_file):
        global LOG_FILE
        LOG_FILE = log_file
        self.server_address, self.client_address = load_config()
        self.my_id = uuid.uuid4()   # Unique identifier for this node
        self.state = 0  # 0 = election ongoing, 1 = leader known
        self.leader_id = None # UUID of elected leader
        self.in_conn = None # Incoming connnection(server)
        self.out_conn = None # Outgoing connection(client)

    def run(self):
        t = threading.Thread(target=self.server_thread)
        t.start()

        time.sleep(1.5) # Ensure server is ready before connecting to client
        self.out_conn = socket(AF_INET, SOCK_STREAM)
        connected = False
        while not connected:
            try:
                self.out_conn.connect(self.client_address)
                connected = True
            except:
                time.sleep(1)
        write_log("Outgoing connection established.")

        init_msg = Message(self.my_id, 0)
        self.send_message(init_msg)

        while self.state == 0:
            time.sleep(1)
        print(f"Leader is decided to {self.leader_id}")
        write_log("Election complete. Exiting.")

    def server_thread(self):
        server_sock = socket(AF_INET, SOCK_STREAM)
        server_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        server_sock.bind(self.server_address)
        server_sock.listen(1)
        write_log(f"Server listening at {self.server_address}")

        conn, addr = server_sock.accept()
        write_log(f"Accepted connection from {addr}")
        self.in_conn = conn

        f = conn.makefile()
        for line in f:
            try:
                msg = Message.from_json(line.strip())
                self.handle_message(msg)
            except Exception as e:
                write_log(f"[ERROR] Message handling error: {e}")
                break
        f.close()
        conn.close()
        server_sock.close()

    def send_message(self, msg):
        while self.out_conn is None:
            time.sleep(1)

        try:
            self.out_conn.send((msg.to_json() + "\n").encode())
            write_log(f"Sent: uuid={msg.uuid}, flag={msg.flag}")
        except Exception as e:
            write_log(f"[ERROR] Send failed: {e}")

    # Handle incoming messages and implements leader election logic
    def handle_message(self, msg):
        # Compare incoming uuid with my_id to determine message relation
        if msg.uuid == self.my_id:
            cmp_result = "same"
        elif msg.uuid > self.my_id:
            cmp_result = "greater"
        else:
            cmp_result = "less"

        if self.state == 1:
            write_log(f"Received: uuid={msg.uuid}, flag={msg.flag},{cmp_result}, 1 (Leader={self.leader_id})")
        else:
            write_log(f"Received: uuid={msg.uuid}, flag={msg.flag},{cmp_result}, 0")

        # Leader election decision making
        if msg.flag == 0:
            if msg.uuid == self.my_id:
                self.state = 1
                self.leader_id = self.my_id
                write_log(f"Leader is decided to {self.leader_id}")
                self.send_message(Message(self.leader_id, 1))
            elif msg.uuid > self.my_id:
                self.send_message(msg)
            else:
                write_log("Ignored")
        elif msg.flag == 1:
            if self.state == 0:
                self.state = 1
                self.leader_id = msg.uuid
                if msg.uuid != self.my_id:
                    self.send_message(msg)
                write_log(f"Leader is decided to {self.leader_id}")
            else:
                write_log(f"Received: uuid={msg.uuid}, flag={msg.flag},{cmp_result}, 1 (Leader={self.leader_id})")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python myleprocess.py <log_filename>")
        sys.exit(1)

    logname = sys.argv[1]
    node = ElectionNode(logname)
    node.run()