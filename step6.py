import socket
import time

host = "hw3.csec380.fun"
port = 380

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((host, port))

request = "POST /delayedPostLogin HTTP/1.1\r\n"
request += "HOST: " + host + "\r\n"
request += "User-Agent: CSEC-380\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request += "Content-Length: 42\r\n\r\n"
request += "username=alice&password=SecretPassword123!\r\n\r\n"

print(request)
sock1.send(request.encode())
response = sock1.recv(4096).decode()
print(response)
sock1.close()

cookie = ""
for line in response.split("\n"):
    if "Cookie:" in line:
        cookie = line.split(";")[0].split(":")[1].strip()
        break
newreq = request.split("\r\n\r\n")
newreq[0] += "\r\nCookie: " + cookie + "\r\n\r\n"
request = newreq[0] + newreq[1]
newreq = request.split("/delayedPostLogin")
newreq[0] += "/delayedPostSecurePage"
request = newreq[0] + newreq[1]
print(request)
time.sleep(30)

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((host, port))
sock2.send(request.encode())

response = sock2.recv(4096).decode()

print(response)
sock2.close()
