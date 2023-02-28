#Lucas Assunção Braga, Leonardo Moussallem de Avila

import threading
import socket
import random

def handle_client(conn, addr):
    print("Conexao aceita de: ", addr)
    # Recebe a solicitação do cliente
    request = conn.recv(1024).decode().strip()
    # Gera uma resposta aleatória "sim" ou "não"
    response = "arquivo existe" if random.random() > 0.5 else "arquivo nao encontrado"
    # Envia a resposta ao cliente
    result = response.encode()
    conn.sendall(result)
    conn.close()

# Configura o socket para o servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 7777))
server_socket.listen(5)

# Recebe continuamente os clientes que chegam e inicia uma nova thread para cada um
while True:
    conn, addr = server_socket.accept()
    t = threading.Thread(target=handle_client, args=(conn, addr))
    t.start()