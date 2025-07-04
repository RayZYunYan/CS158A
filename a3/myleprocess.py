from socket import *
import threading
import uuid
import json
import time
import sys

# Configuration
CONFIG_FILE = "config.txt"
LOG_FILE = None

# Message class
class Message:
    def __init__(self, uuid_val, flag):
        self.uuid = uuid_val
        self.flag = flag # 0 for still electing, 1 for leader elected

    def to_json(self): # Convert message to JSON string
        return json.dumps({
            "uuid": str(self.uuid),
            "flag": self.flag
        })

    @staticmethod
    def from_json(s): # Convert JSON string to Message object
        data = json.loads(s)
        return Message(uuid.UUID(data["uuid"]), data["flag"])
    
# Log function
def write_log(line):
    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")
    print(line)

# Load configuration from file and return server and client addresses
def load_config():
    with open(CONFIG_FILE, "r") as f:
        lines = f.read().splitlines()
        server_ip, server_port = lines[0].split(",")
        client_ip, client_port = lines[1].split(",")
        return (server_ip.strip(), int(server_port.strip())), (client_ip.strip(), int(client_port.strip()))  

# Election process
class ElectionNode:
    def __init__(self, log_file):
        global LOG_FILE
        LOG_FILE = log_file
        self.server_address, self.client_address = load_config()
        self.my_id = uuid.uuid4() # Generate a unique UUID for this node
        self.state = 0
        self.leader_id = None
        self.in_conn = None
        self.out_conn = None
        self.lock = threading.Lock()

    def run(self): # Start the server and wait for last node to connect
        t = threading.Thread(target=self.server_thread)
        t.start()

        time.sleep(1)  # Ensure server is ready before client starts

        # Connect to next node as client
        self.out_conn = socket(AF_INET, SOCK_STREAM)
        connected = False
        while not connected:
            try:
                self.out_conn.connect(self.client_address)
                connected = True
            except:
                time.sleep(1)

        # Initiate message: send my UUID
        init_msg = Message(self.my_id, 0)
        self.send_message(init_msg)

        # Wait until election is complete
        while self.state == 0:
            time.sleep(1)

    def server_thread(self):
        server_sock = socket(AF_INET, SOCK_STREAM)
        server_sock.bind(self.server_address)
        server_sock.listen(1)
        conn, addr = server_sock.accept()
        self.in_conn = conn

        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
                msg = Message.from_json(data.decode())
                self.handle_message(msg)
            except Exception as e:
                write_log(f"[ERROR] Server receive error: {e}")
                break

    def send_message(self, msg):
        if self.out_conn is None:
            write_log("[ERROR] Outgoing connection not established.")
            return
        try:
            self.out_conn.send(msg.to_json().encode())
            write_log(f"Sent: uuid={msg.uuid}, flag={msg.flag}")
        except Exception as e:
            write_log(f"[ERROR] Send failed: {e}")


    def handle_message(self, msg):
        with self.lock:
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

            if msg.flag == 0: 
                if msg.uuid == self.my_id:
                    # UUID returned to self: I am the leader
                    self.state = 1
                    self.leader_id = self.my_id
                    write_log(f"Leader is decided to {self.leader_id}")
                    leader_msg = Message(self.leader_id, 1)
                    self.send_message(leader_msg)
                elif msg.uuid > self.my_id:
                    self.send_message(msg)
                else:
                    write_log("Ignored")
            elif msg.flag == 1:
                self.state = 1
                self.leader_id = msg.uuid
                if msg.uuid != self.my_id:
                    self.send_message(msg)
                write_log(f"Leader is decided to {self.leader_id}")

# --- Main Entry Point ---
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python myleprocess.py <log_filename>")
        sys.exit(1)

    logname = sys.argv[1]
    node = ElectionNode(logname)
    node.run()