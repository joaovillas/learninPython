from urllib.request import  urlopen as uReq
from bs4 import BeautifulSoup as soup
import urllib.error

cep = input('Digite o cep:')

url ='https://viacep.com.br/ws/'+cep+'/xml/'
try:
    pagina_xml = uReq(url)
    pagina = pagina_xml.read()
    pagina_xml.close()
    pagina_soup = soup(pagina,'html.parser')

    cepx = pagina_soup.find('cep').text
    logradouro = pagina_soup.find('logradouro').text
    bairro = pagina_soup.find('bairro').text
    localidade = pagina_soup.find('localidade').text
    estado = pagina_soup.find('uf').text

    print('---------------------'+localidade+'---------------------')
    print('cep:'+cepx)
    print('logradouro:'+logradouro)
    print('bairro:'+bairro)
    print('Localidade:'+localidade)
    print('Estado:'+estado)
except urllib.error.HTTPError:
    print('CEP INEXISTENTE')
except KeyError :
    print('Cep INEXISTENE')
except AttributeError :
    print ('CEP NAO ENCONTRADO')