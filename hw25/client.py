import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 3000

socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    user_message = input("Enter your message: ")

    socket_.sendto(user_message.encode(), ("127.0.0.1", 3000))
    response, _ = socket_.recvfrom(1024)

    print(f"Відповідь сервера - {response.decode()}.")
