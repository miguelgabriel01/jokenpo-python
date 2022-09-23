import socket
import random

HOST = 'localhost' # Nome do servidor
PORT = 5005 # porta do servidor
addr = (HOST, PORT)

opcoesJogadas = ['Pedra', 'Papel', 'Tesoura'] # lista com possiveis jogadas

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET declara a familia dos protocolos / SOCKET_STREAM indica que será tcp/ip

sock.bind(addr) # Define para qual IP e porta o servidor deve aguardar comexão

sock.listen(5) # Define o limute de conexões

print("Aguardando conexão de um cliente:")

conn, ender = sock.accept() # Conexão e endereço

print('Connectado com', ender) # Apresenta o endereço do cliente com o nome do host e a porta que foram cnectados

print("\nOs palpites do servidor são ALEATÓRIOS!\n")

while True: # O servidor fica liberado por tempo indeterminado ou até a conexão ser encerrada

    # Aguada o retorno do servidor( um dado enviado pela rede de até 1024 bytes ), a função recv possui somente 1 argumento que é o tamho do buffer
    data = conn.recv(1024) 

    if not data: # Quando não tiver mais nada dentro da var data, a coneção é encerrada
        print("\nConexão encerrada!\n")

        conn.close() # Serve para encerrar a conexão entre as aplicações
        break
    
    palpiteClient = str(data.decode()) # Ultilizada para decodificar e transformar a mensgem enviada pelo cliente em uma String
    palpiteServ = random.choice(opcoesJogadas) # O palpite do servidor é escolhido de forma randomica

    print("* O Servidor respondeu:", palpiteServ) 

    # Verifica quando o cliente ganha a jogada
    if ((palpiteClient == 'Tesoura' and palpiteServ == 'Papel') or (palpiteClient == 'Pedra' and palpiteServ == 'Tesoura') or (palpiteClient == 'Papel' and palpiteServ == 'Pedra')):
        ganhador = 'Cliente'
    
    # Verifica quando o servidor ganha a jogada
    if ((palpiteClient == 'Papel' and palpiteServ == 'Tesoura') or (palpiteClient == 'Tesoura' and palpiteServ == 'Pedra') or (palpiteClient == 'Pedra' and palpiteServ == 'Papel')):
        ganhador = 'Servidor'
    
    # Verifica quando existe um empate
    if (palpiteClient == palpiteServ):
        ganhador = 'Empate'

    result = '- Cliente: '+ str(palpiteClient) + '\n - Servidor: ' + str(palpiteServ) + '\n=> GANHADOR: ' + str(ganhador) + '\n' # Concatenação dos resultados, sendo eles apresentados para o cliente

    # Envia o resultado para o cliente
    conn.sendall(bytes(str(result), 'utf8'))