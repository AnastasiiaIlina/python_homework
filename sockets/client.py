import requests

response = requests.get('https://api.github.com/', params={'q': 'requests+language:python'},)

# print(response.json()['user_url'])
# print(response.headers['Content-Type'])

response.json() 









# import socket

# HOST = "127.0.0.1"
# PORT = 3001

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.connect((HOST, PORT))
#     s.sendall(b"Hello, world")
#     data = s.recv(1024)

# print(f"Received {data!r}")