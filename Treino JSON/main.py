import json
import string

cont= True
fabrica = {}
f = open('fabrica.json','a')

while (cont == True):

    funcionario ={}
    info_dados = {}
    info_basico = {}



    nome = input('NOME:')
    sexo = input('SEXO:')
    data_nasc = input('Data de Nascimento:')

    rg = input('RG:')
    cpf = input('CPF:')
    telefone = input('TELEFONE:')


    info_basico['Sexo:'] = sexo
    info_basico['Data de Nascimento:'] =data_nasc
    info_dados['RG'] = rg
    info_dados['CPF'] = cpf
    info_dados['Telefone'] = telefone


    funcionario['Dados'] = info_dados
    funcionario['Info Basicas'] = info_basico

    fabrica[nome] = funcionario





    resp = input('Deseja Continuar?')


    if resp.lower() =='s' :
        cont = True
    elif resp.lower() =='n':
        cont = False
    else:
        print('Digite uma Opcao Valida')






fabrica_string = json.dumps(fabrica,ensure_ascii=False,sort_keys=True,indent=4 )
f.write(fabrica_string)
f.close()