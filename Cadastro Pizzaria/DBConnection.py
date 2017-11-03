import sqlite3

conn = sqlite3.connect('Pizzaria.db')


def create( nome, telefone , endereco , cep):
    nome = str.upper(nome)
    endereco = str.upper(endereco)

    try:
        conn.execute('insert into Clientes values ("'+nome+'","'+telefone+'","'+endereco+'", "'+cep+'")')
        conn.commit()
    except TypeError:
        print('Digite os campos para Criar ')
def read ():
    nav = conn.execute('Select nome , telefone , endereco , cep from Clientes; ')

    rows = nav.fetchall()

    print('===============Clientes===============')
    for row in rows:
        print(row)


def update( nome ,endereco , cep , telefone):
    try:
        conn.execute('UPDATE Clientes SET endereco = "'+endereco+'" ,cep ="'+cep+'", telefone ="'+telefone+'" WHERE nome = "'+nome+'";')
        conn.commit()
    except TypeError:
        print('Digite os campos para atualizar')

def delete (nome):
    try:
        conn.execute('DELETE FROM Clientes WHERE nome = "'+nome+'";')
        conn.commit()
    except TypeError :
        print('Digite o nome para deletar')
    except TypeError:
        print('error')








