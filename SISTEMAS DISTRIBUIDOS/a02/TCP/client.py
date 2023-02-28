#Lucas Assunção Braga, Leonardo Moussallem de Avila

import socket

# Estabelece conexão com o servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 7777))

# Envia a solicitação ao servidor
request = "sim ou nao".encode()
client_socket.sendall(request)

# Recebe a resposta do servidor
response = client_socket.recv(1024).decode().strip()

# Exibe a resposta
print("Resposta:", response)

client_socket.close()