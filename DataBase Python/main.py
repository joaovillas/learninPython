import sqlite3

conn = sqlite3.connect('ProjetoPython.db')

#Criando Funcoes para o banco

def create(usuario, senha):
    conn.execute('insert into Usuarios values ("'+usuario+'","'+senha+'")')
    conn.commit()

def read ():
    nav = conn.execute('Select usuario , senha from Usuarios; ')
    rows = nav.fetchall()
    print(rows)


def update(usuario,senha):

     conn.execute('UPDATE Usuarios SET senha = "'+senha+'" WHERE usuario = "'+usuario+'";')
     conn.commit()

def delete (usuario):
    conn.execute('DELETE FROM Usuarios WHERE usuario = "'+usuario+'";')
    conn.commit()

# MAIN

usuario = input('usuario:')
senha = input('senha:')

create(usuario,senha)
read()







conn.close()