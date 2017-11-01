'''
Lado do cliente : Usa sockets para mandar data para o servidor , e imprime
a resposta do servidor para cada linha na mensagem. Podemos Colocar o host
como sendo localhost para indicar que o servidor esta na mesma maquina
Para rodar através da internet é preciso colocar o servidor em outra máquina
e passar para o nome do host o endereço de ip ou nome do domínio.
'''

from socket import *

#Configuracoes de conexao do servidor
#O nome do servidor pode ser o endereco de
#IP ou domínio (ola.python.net)

serverhost = 'localhost'
port = 5001

#mensagem a ser mandada codificada em bytes


mensagem = input('Digite a mensagem pro servidor')
mensagem = bytes(mensagem,'utf-8')
#criamos um socket e o conectamos ao servidor

sockobj = socket(AF_INET,SOCK_STREAM) #TCP/IP
sockobj.connect((serverhost,port))

#mandamos a mensagem linha por linha

sockobj.send(mensagem)

#depois mandar uma linha esperamos a resposta do server
data = sockobj.recv(1024)
print('O servidor respondeu :'+repr(data))
sockobj.close()