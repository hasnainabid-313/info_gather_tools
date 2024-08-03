import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = input("Enter IP: ")
port = int(input("Enter PORT: "))

try:
    s.connect((ip, port))
    result = s.recv(2048).decode()
    print("Received:", result)
except socket.error as e:
    print(f"Socket error: {e}")
finally:
    s.close()
