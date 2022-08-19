"""
1) Создайте клиента, который отправляет серверу из предыдущего упражнения число 5, затем ещё число 10
и затем команду «exit».
2) Убедитесь, что всё работает правильно, то есть сервер после первой команды должен прислать «50», после второй –
«100», а после команды «exit» должен быть остановлен (то есть программа из предыдущего упражнения должна остановиться).
"""

import socket

SERVER_ADDRESS = ('localhost', 15253)

client = socket.socket()
client.connect(SERVER_ADDRESS)
client.send(bytes("stop", encoding="UTF-8"))
data = client.recv(4096)
data = data.decode("UTF-8")
print(data)
