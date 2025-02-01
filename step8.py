import socket
import re

host = "hw3.csec380.fun"
port = 380

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((host, port))

request = "POST /captchaLogin HTTP/1.1\r\n"
request += "HOST: " + host + "\r\n"
request += "User-Agent: CSEC-380\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request += "Content-Length: 42\r\n\r\n"
request += "username=alice&password=SecretPassword123!\r\n\r\n"

print("request 1:\n" + request)
sock1.send(request.encode())
response = sock1.recv(4096).decode()
print("response 1:\n" + response)
sock1.close()

content = response.split("\r\n\r\n")[1]
values = re.findall(r'\d+', content)
result = 0
if '-' in content:
    result = int(values[0]) - int(values[1])
elif '+' in content:
    result = int(values[0]) + int(values[1])
elif '*' in content:
    result = int(values[0]) * int(values[1])
else:
    result = int(values[0]) / int(values[1])

cookie = ""
for line in response.split("\n"):
    if "Cookie:" in line:
        cookie = line.split(";")[0].split(":")[1].strip()
        break
content = "solution=" + str(result) + "\r\n\r\n"

request = "POST /captchaValidate HTTP/1.1\r\n"
request += "HOST: " + host + "\r\n"
request += "User-Agent: CSEC-380\r\n"
request += "Cookie: " + cookie + "\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request += "Content-Length: " + str(len(content) - 4) + "\r\n\r\n"
request += content
print("request 2:\n" + request)

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((host, port))
sock2.send(request.encode())

response = sock2.recv(4096).decode()

print("response 2:\n" + response)
sock2.close()


request = "POST /captchaSecurePage HTTP/1.1\r\n"
request += "HOST: " + host + "\r\n"
request += "User-Agent: CSEC-380\r\n"
request += "Cookie: " + cookie + "\r\n"
request += "Content-Type: application/x-www-form--urlencoded\r\n"
request += "Content-length: " + str(len(content) - 4) + "\r\n\r\n"
request += content
print("reqest 3:\n" + request)

sock3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock3.connect((host, port))
sock3.send(request.encode())
response = sock3.recv(4096).decode()
print("response 3:\n" + response)
sock3.close()
