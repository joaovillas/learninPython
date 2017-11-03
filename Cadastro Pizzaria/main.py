import DBConnection
import APICEP
import sqlite3



conn = sqlite3.connect('Pizzaria.db')
db = DBConnection
finder = APICEP

escolha = -1

while escolha != 5:
    print ('1- Cadastro Clientes')
    print ('2- Visualizar Clientes')
    print ('3- Apagar Cliente')
    print ('4- Atualizar Cadastro')
    print ('5- Sair')
    escolha = int(input('Numero:'))

    if escolha ==1 :
        nome = input('Nome: ')
        cep = input('CEP: ')
        info_json=finder.buscacep(cep)
        numero = input('Numero:')
        endereco = info_json['logradouro']+', numero: '+numero+' ,'+info_json['bairro']
        telefone = input('Telefone:')
        db.create (nome,telefone,endereco,cep)
    elif escolha ==2:
        db.read()
    elif escolha ==3:
        nome = input('Nome:')
        db.delete(nome)
    elif escolha ==4:
        nome = input('Nome:')
        cep = input('CEP:')
        info_json = finder.buscacep(cep)
        numero = input('Numero:')
        endereco = info_json['logradouro'] + ', numero: ' + numero + ' ,' + info_json['bairro']
        telefone = input('Telefone:')
        db.update(nome ,endereco ,cep ,telefone)
    elif escolha ==5:
        print('Saindo do programa ')

    else :
        print('Digite uma opcao Válida')

conn.close()



