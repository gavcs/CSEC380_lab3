import socket

host = "hw3.csec380.fun"
path = "/basic"
port = 380

request = (
    f"GET {path} HTTP/1.1\r\n"
    f"HOST: {host}\r\n"
    "User-Agent: CSEC-380\r\n"
    "Authorization: Basic YWxpY2U6U2VjcmV0UGFzc3dvcmQxMjMh\r\n"
    "\r\n"
)

print("The request sent:\n" + request)

request = request.encode()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
sock.send(request)


print("The response received:")
print(sock.recv(4096).decode())
sock.close()
