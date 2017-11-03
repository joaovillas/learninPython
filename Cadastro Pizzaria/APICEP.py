from urllib.request import urlopen as uReq
import json
import urllib.error


def buscacep(cep):

    cep = cep.replace(' ','')
    cep = cep.replace('-','')
    cep = cep.replace('_','')

    url = 'https://viacep.com.br/ws/'+cep+'/json/ '

    #abre conexão com a pagina
    try:
        pagina_html = uReq(url) #Vai ir na url
        pagina = pagina_html.read() #vai ler a pagina
        pagina_html.close() #fecha a pagina

        pagina_json = json.loads(pagina)

        return  pagina_json

    except urllib.error.HTTPError:
        print('CEP INEXISTENTE')
    except KeyError :
        print('Cep INEXISTENE')

