'''
Sockets - Interfaces programáveis de comunicação entre softwares
que podem estar rodando em computadores distintos na rede.
Permitem transferir strings em bytes de um processo pra outro e é
a base da maioria dos protocolos de alto nível , como FTP ,
Páginas da web e email

Lado do servidor : Abre um TCP / IP numa port , espera por uma
mensagem de um cliente , e manda essa mensagem de volta como resposta.
Esse é uma simples ouve/responde conversação por cliente, mas percorre
um loop infinito para ouvir por mais clientes enquanto o script do server
estiver rodando . O cliente pode rodar em outra máquina ou no mesmo computador
se usar o 'locahost' como servidor .

'''



from socket import *
import time

#cria o nome do host
meuHost = ''

#Utiliza este numero de porto
port = 50007
#Cria um objeto Socket . As duas constantes referentes a
#Familia do endereço (Padrão é Socket.AF_INET)
#Se é Stream (socket.SOCK_STREAM , o padrão ) ou datagram (socket.SOCK_DGRAM)
#E o protocolo (Padrão é 0)
#Da maneia como configuramos :
#AF_INIT == PROTOCOLO DE ENDEREÇO DE IP
#SOCK_STREAM == PROTOCOLO DE TRANSFERENCIA TCP
#COMBINAÇÃO ==> SERVER TCP/IP
sockobj = socket(AF_INET,SOCK_STREAM)

#Vincula o servidor ao numero de porto
sockobj.bind((meuHost,port))

#O socket começa a esperar por clientes limitando a
#5 Conexões por vez

sockobj.listen(5)

while True:
    #Aceita uma conexão quando encontrada e devolve a
    #um novo socket conexão e o endereço do cliente
    #conectado
    conexao , endereco = sockobj.accept()
    print('Server conectado por '+repr(endereco))

    while True :
        #Recebe data enviada pelo cliente
        data = conexao.recv(1024)
        time.sleep(3)

        #Se nao receber nada paramos o loop
        if not data: break

        #O servidor manda de volta uma resposta
        conexao.send(data)
    #fecha conexão
    conexao.close()












