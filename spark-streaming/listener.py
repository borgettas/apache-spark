import socket
import time


HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT))
print(f'Waiting connection: {PORT}')

s.listen(5)
conn, address = s.accept()
print(f'Received solicitation from {address}')

messages = [
    'Message A',
    'Message B',
    'Message C',
    'Message D',
    'Message E',
    'Message F',
    'Great'
]

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(4)

conn.close()