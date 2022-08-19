"""
1) Создайте сервер, который получает число, умножает его на 10 и отправляет обратно клиенту.
2) При получении команды «stop», сервер должен быть остановлен (в примере из урока это можно сделать, завершив
бесконечный цикл с помощью break).
"""
import socket

SERVER_ADDRESS = ("", 15253)

server = socket.socket()
server.bind(SERVER_ADDRESS)
server.listen(3)
print("Wait client")
while True:
    d, i = server.accept()
    data = d.recv(4096)
    data = data.decode("UTF-8")
    print("From client has", data)
    if data == "stop":
        print("Stop by client")
        break
    else:
        data = int(data) * 10
        d.send(bytes(str(data), encoding="UTF-8"))
    d.close()
