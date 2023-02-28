#Lucas Assunção Braga, Leonardo Moussallem de Avila

import socket
import random

answers = {"resposta1": "correta", "resposta2": "incorreta", "resposta3": "correta"}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("0.0.0.0", 12345))

while True:
    data, client_address = server_socket.recvfrom(1024)
    answer = data.decode().strip()
    result = answers.get(answer, "incorreta")
    if random.random() > 0.5:
        result = "incorrect"
    print("recebe a resposta: %s, resultado: %s" % (answer, result))
    server_socket.sendto(result.encode(), client_address)