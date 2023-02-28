import socket

def main():
    # Endereço IP e porta do servidor
    host = '127.0.0.1'
    port = 5000
    
    # Criação do socket UDP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    
    print('Servidor esperando por conexões...')
    
    while True:
        # Recebe os datagramas do cliente
        data, address = s.recvfrom(1024)
        
        # Decodifica os dados recebidos
        question_number, number_of_answers, answers = data.decode().split(';')
        
        # Calcula o número de acertos e erros
        correct_answers = answers.count('V')
        wrong_answers = len(answers) - correct_answers
        
        # Envia a resposta para o cliente
        response = f'{question_number};{correct_answers};{wrong_answers}'
        s.sendto(response.encode(), address)
        
        # Fecha a conexão com o cliente
        print(f'Conexão encerrada com {address}')

if __name__ == '__main__':
    main()