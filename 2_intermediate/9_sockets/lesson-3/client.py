import socket

HEADER = 64
FORMAT = 'utf8'
PORT = 1002
DISCONNECT = 'disconnect'

HOST = '192.168.100.19'
ADDR = (HOST, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


send('Hello')
input()
send('Hello')
input()
send('Hello')
input()
send('Hello')
input()
send(DISCONNECT)