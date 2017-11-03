from socket import *
import threading


class Cliente(threading.Thread):
    '''
    Classe que gera os Clientes
    '''

    def __init__(self, c, server, port, mensagem):
        # Numero de identificacao do cliente
        self.c = c

        # Servidor a ser conectado
        self.server = server

        # Port pra ser usada
        self.port = port

        # mensagens a serem colocadas
        self.msgs = mensagem

        threading.Thread.__init__(self)

    def run(self):
        #Cria-se o socket e o conectamos ao servidor
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.server, self.port))

        for linha in self.msgs:
            sockobj.send(linha)

            #Depois de mandar uma linha esperamos uma resposta do servidor
            data = sockobj.recv(1024)
            print('Cliente'+repr(self.c)+' Recebeu: '+repr(data))

        sockobj.close()



serverHost = 'localhost'
serverPort = 50007

try :

    mensagem = [b'Ola mundo!']
    for c in range(10):
        Cliente(c , serverHost,serverPort, mensagem).start()
    print('Geramos todos os clientes')

except ConnectionRefusedError:
    print('Erro ao se conectar ao servidor')
except WindowsError :
    print('Erro ao se conectar ao servidor')