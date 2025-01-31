import socket

host = "hw3.csec380.fun"
port = 380

sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock1.connect((host, port))

request = "POST /jsonLogin HTTP/1.1\r\n"
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

key = response.split("\r\n\r\n")[1].split(":")[2]
key = key.strip("}").strip().strip("\"")
key = "apikey=" + key + "\r\n\r\n"
cookie = ""
for line in response.split("\n"):
    if "Cookie:" in line:
        cookie = line.split(";")[0].split(":")[1].strip()
        break
request = "POST /jsonSecurePage HTTP/1.1\r\n"
request += "HOST: " + host + "\r\n"
request += "User-Agent: CSEC-380\r\n"
request += "Cookie: " + cookie + "\r\n"
request += "Content-Type: application/x-www-form-urlencoded\r\n"
request += "Content-Length: " + str(len(key) - 4) + "\r\n\r\n"
request += key
print(request)

sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2.connect((host, port))
sock2.send(request.encode())

response = sock2.recv(4096).decode()

print(response)
sock2.close()
