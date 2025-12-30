import socket
import threading
from chatbot import send_chat_message, initialize_chat

# Fixed message size for all communications
MSG_LENGTH = 1024
PORT = 5050
# SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '127.0.0.1' # Listen on all interfaces
ADDR = (SERVER, PORT) # (127.0.0.1, 5050)
FORMAT = 'utf-8'
DISCONNECT_MESSAGES = ["exit", "quit"]

def recv_all(conn, n):
    """Receive exactly n bytes or return None if the connection closed."""
    data = b''
    while len(data) < n:
        packet = conn.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    initialize_chat(addr)
    try:
        while True:
            msg_bytes = recv_all(conn, MSG_LENGTH)
            if msg_bytes is None:
                print(f"[DISCONNECT] {addr} closed connection.")
                break

            msg = msg_bytes.rstrip(b'\0').decode(FORMAT)
            if not msg.strip():
                continue
            
            if msg in DISCONNECT_MESSAGES:
                print(f"[DISCONNECT MSG] {addr} requested disconnect.")
                break

            print(f"[{addr}] {msg}")
            reply = send_chat_message(msg, addr)
            if reply == 429:
                reply = "Error: Not enough quota to process the request."
                print(f"[QUOTA EXCEEDED] {addr}")
            else:
                print(f"[Chatbot returned] {addr}")
            
            reply_bytes = reply.encode(FORMAT)[:MSG_LENGTH]  # truncate if too long
            if len(reply_bytes) < MSG_LENGTH:
                reply_bytes = reply_bytes.ljust(MSG_LENGTH, b'\0')  # pad with nulls
            conn.sendall(reply_bytes)
    except ConnectionResetError:
        print(f"[RESET] Connection reset by {addr}")
    except Exception as e:
        print(f"[ERROR] {addr} - {e}")
    finally:
        conn.close()
        print(f"[CLOSED] {addr} connection closed")

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()