import socket

# declare destination information
host = "hw3.csec380.fun"
port = 380

'''
    form the GET request to the host, then print, format, and send
    User-Agent is required
'''
request = (
    "GET /getLogin?username=alice&password=SecretPassword123! HTTP/1.1\r\n"
    "HOST: " + host +"\r\n"
    "User-Agent: CSEC-380\r\n"
    "\r\n"
)
print("The request sent:\n" + request)
request = request.encode()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(request)

# print the response to the request
response = sock.recv(4096).decode()
print("The response received:")
print(response, flush=True)
sock.close()

# get the cookie from the response
response = response.split("\n")
cookie = ""
for line in response:
    if "Cookie:" in line:
        cookie = line.split(";")[0].split(":")[1].strip()
        break

# form the new request and socket
request = (
    "GET /getSecurePage HTTP/1.1\r\n"
    "HOST: " + host + "\r\n"
    "User-Agent: CSEC-380\r\n" +
    "Cookie: " +cookie + "\r\n"
    "\r\n"
)
print("\nThe next request sent:\n" + request)
request = request.encode()
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((host, port))
sock2.send(request)
response = sock2.recv(4096)

# close the sockets
sock2.close()

print("The response received:")
print(response.decode())
