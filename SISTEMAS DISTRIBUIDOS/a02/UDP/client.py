#Lucas Assunção Braga, Leonardo Moussallem de Avila

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

answers = ["resposta1", "resposta2", "resposta3"]

for answer in answers:
    client_socket.sendto(answer.encode(), ("127.0.0.1", 12345))

    data, server_address = client_socket.recvfrom(1024)
    result = data.decode().strip()
    print("recebe o resultado: %s para a resposta: %s" % (result, answer))