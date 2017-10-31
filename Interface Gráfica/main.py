#==================
#=== JOAO PEDRO ===
#==================

#mainloop = laço de repetiçao enquanto a janela é exibida

from tkinter import *

def bt_click():
    print('Clicou xDxDxD')

    lb["text"] = "Funcionou"



janela = Tk()
janela.title('Janela Principal')
janela["bg"] = "gray"

bt = Button(janela,width=30,text='Enviar',command=bt_click)
bt.place (x=550,y=500)

lb= Label(janela , text="clique aqui" )
lb.place (x=550,y=470)
lb["bg"] = 'gray'
# Width x Height + Left + Top
janela.geometry('800x600+500+175')
janela.mainloop() ## vai passar de linha quando a janela for fechada

