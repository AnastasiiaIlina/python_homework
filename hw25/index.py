import socket

# UDP-комунікація:
# Створіть простий UDP-сервер, який може приймати дані від клієнтів.
# Напишіть клієнтський додаток, який відправляє дані на сервер та очікує відповіді.
# * потрібно буде використати функцію recvfrom() замість recv() як це було для TCP протоколу реалізовано

HOST = "127.0.0.1"
PORT = 3000

socket_ = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM)
socket_.bind((HOST, PORT))

while True:
    data, client_address = socket_.recvfrom(1024)

    print(f"Повідомлення з веб-клієнта: {client_address}: {data.decode()}")

    response = "Дані успішно отримано!"
    socket_.sendto(response.encode(), client_address)

