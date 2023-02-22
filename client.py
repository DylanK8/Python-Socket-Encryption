from cryptography.fernet import Fernet
import socket

key = b'PUT YOUR KEY HERE'

HOST = "<IP-ADDRESS>"
PORT = <PORT>

msg = input("input your data:")

fernet = Fernet(key)


encMsg = fernet.encrypt(msg.encode())
print("original string: ", msg)
print("encrypted string: ", encMsg)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(encMsg)
    data = s.recv(1024)
    decMessage = fernet.decrypt(data).decode()
print(f"Received {decMessage!r}")
