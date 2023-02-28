import socket

def main():
    # Endereço IP e porta do servidor
    host = '127.0.0.1'
    port = 5000
    
    # Criação do socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Dados a serem enviados ao servidor
    data = [
        '1;3;VVF', 
        '2;4;VFFF', 
        '3;2;VF'
    ]
    
    for d in data:
        # Envia os dados para o servidor
        s.sendto(d.encode(), (host, port))
        
        # Recebe a resposta do servidor
        response, address = s.recvfrom(1024)
        
        # Exibe a resposta recebida
        print(response.decode())
    
    # Fecha a conexão com o servidor
    s.close()

if __name__ == '__main__':
    main()