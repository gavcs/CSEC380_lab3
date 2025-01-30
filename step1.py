import socket

host = "hw3.csec380.fun"
path = "/hello"
port = 380

request = (
    f"GET {path} HTTP/1.1\r\n"
    f"HOST: {host}\r\n"
    "Connection: keep-alive\r\n"
    "\r\n"
)

print("The request sent:\n" + request)

request = request.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
sock.send(request)

data = sock.recv(4096)

print("The response received:\n" + data.decode())
sock.close()
