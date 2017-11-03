from urllib.request import urlopen as uReq
import json
import urllib.error
cep = input('Digite seu CEP:')
cep = cep.replace(' ','')

permission = False


url = 'https://viacep.com.br/ws/'+cep+'/json/ '

#abre conexão com a pagina
try:
    pagina_html = uReq(url) #Vai ir na url
    pagina = pagina_html.read() #vai ler a pagina
    pagina_html.close() #fecha a pagina

    pagina_json = json.loads(pagina)


    print('CEP: '+pagina_json['cep'])
    print('logradouro: '+pagina_json['logradouro'])
    print('bairro: '+pagina_json['bairro'])
    print('Localidade '+pagina_json['localidade'])
    print('Estado:'+pagina_json['uf'])
except urllib.error.HTTPError:
    print('CEP INEXISTENTE')
except KeyError :
    print('Cep INEXISTENE')

