import socket

# Fixed message size for all communications
MSG_LENGTH = 1024
PORT = 5050
FORMAT = 'utf-8'
SERVER = '127.0.0.1' # localhost
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def recv_all(conn, n):
    """Receive exactly n bytes or return None if the connection closed."""
    data = b''
    while len(data) < n:
        packet = conn.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

def send(msg):
    message = msg.encode(FORMAT)[:MSG_LENGTH]  # truncate if too long
    if len(message) < MSG_LENGTH:
        message = message.ljust(MSG_LENGTH, b'\0')  # pad with nulls
    client.sendall(message)
    return 0

def recieve():
    resp = recv_all(client, MSG_LENGTH)
    if resp is None:
        return None
    return resp.rstrip(b'\0').decode(FORMAT)

print("Client is ready to send messages. Type exit or quit to disconnect.")
while True:
    print("-"*40)
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        send(user_input)
        break
    if not user_input.strip():
        print("Please type a message.")
        continue
    if not send(user_input):
        reply = recieve()
        if reply:
            print(f"\nChatbot: {reply}")
        else:
            print("No response from server.")
            client.close()
