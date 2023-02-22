from cryptography.fernet import Fernet
import socket

key = b'PUT YOUR KEY HERE'

fernet = Fernet(key)

HOST = "<IP-ADDRESS>"
PORT = <PORT>

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(<PORT>)
            if not data:
                break
            decMessage = fernet.decrypt(data).decode()
            print("Received data: ", data)
            print("Decrypted message: ", decMessage)
            conn.sendall(data)
