import socket
import random

HOST = '127.0.0.1' # Nome do cliente
PORT = 5005 # porta do servidor

opcoesJogadas = ['Pedra', 'Papel', 'Tesoura'] # lista com as possiveis jogadas que podem ser escolhidas

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET declara a familia dos protocolos / SOCKET_STREAM indica que será tcp/ip

sock.connect((HOST, PORT)) # AF_INET declara a familia dos protocolos / SOCKET_STREAM indica que será tcp/ip

while True: # o cliente tem a opção de realizar varias conexões com o servidor até essa conexão estiver de pé 
    opcao1 = int(input("\n* Escolha uma opção:\n 1- Palpite aleatório\n 2- Informar um palpite\n 0- Para encerrar.\n -> Opcao: ")) # Menu para o usuario escolher sua opção

    if (opcao1 == 1):
        mensagemEnvioClient = random.choice(opcoesJogadas) # Faz um random de acordo com as jogadas pré criadas

    if (opcao1 == 2):
        opcao2 = int(input("\n* Ecolha o palpite:\n 1- Pedra\n 2- Papel\n 3- Tesoura\n -> Opcao: "))

        if (opcao2 == 1):
            mensagemEnvioClient = 'Pedra' 
        elif (opcao2 == 2):
            mensagemEnvioClient = 'Papel' 
        elif (opcao2 == 3):
            mensagemEnvioClient = 'Tesoura' 
    
    if (opcao1 == 0):
        print("\nConexão encerrada!\n")

        sock.close() # funçaõ ultilizada para encerrar a conexão entre as duas aplicações
        break
    
    sock.sendall(str.encode(mensagemEnvioClient)) # Envia mensagens para o servidor
    
    print("\n-> Palpite enviado pelo cliente: ", mensagemEnvioClient) 

    # Aguada o retorno do servidor( um dado enviado pela rede de até 1024 bytes ), a função recv possui somente 1 argumento que é o tamho do buffer
    data = sock.recv(1024) 

    print('\n*** Resultado final do jogo: \n', data.decode().upper()) # Decodifica a mensagem recebida pelo servidor, coloca todas as letras em caixa alta e exibe a mensagem