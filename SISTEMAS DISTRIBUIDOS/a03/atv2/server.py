import socket
import threading
import os

HOST = '127.0.0.1'  # Endereço do servidor
PORT = 8000  # Porta do servidor
BUFFER_SIZE = 1024  # Tamanho do buffer de leitura

def handle_client(conn, addr):
    print(f'Conexão estabelecida com {addr}')
    while True:
        # Recebe o nome do arquivo solicitado pelo cliente
        filename = conn.recv(BUFFER_SIZE).decode()
        if not filename:
            break
        # Verifica se o arquivo existe
        if os.path.isfile(filename):
            # Abre o arquivo e envia seu conteúdo para o cliente em pacotes de tamanho BUFFER_SIZE
            with open(filename, 'rb') as f:
                data = f.read(BUFFER_SIZE)
                while data:
                    conn.send(data)
                    data = f.read(BUFFER_SIZE)
        else:
            # Se o arquivo não existir, envia uma mensagem informando o cliente
            conn.send(b'Arquivo não encontrado')
    print(f'Conexão encerrada com {addr}')
    conn.close()

def run_server():
    # Cria um socket TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Liga o socket ao endereço e porta definidos
        s.bind((HOST, PORT))
        # Escuta por conexões
        s.listen()
        print(f'Servidor iniciado em {HOST}:{PORT}')
        while True:
            # Aceita uma conexão
            conn, addr = s.accept()
            # Inicia uma nova thread para lidar com o cliente
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    run_server()