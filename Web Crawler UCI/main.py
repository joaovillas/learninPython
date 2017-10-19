from urllib.request import urlopen as uReq  
from bs4 import BeautifulSoup as soup 


def validador( valida ):
    valida.replace('ã','a')
    valida.replace('õ', 'o')
    valida.replace('á','a')
    valida.replace('é', 'e')
    valida.replace('í', 'i')
    valida.replace('ó', 'o')
    valida.replace('ú', 'u')

    print(valida)
    return valida



my_url = 'http://www.orientcinemas.com.br/programacao/8/uci-orient-shopping-da-bahia.html'

cliente = uReq(my_url)

pagina_html = cliente.read()
cliente.close()

pagina_soup = soup(pagina_html,'html.parser')


containers = pagina_soup.findAll('div',{'class':'sh-horarios'})


nomearquivo = 'filmes.txt'
f=open(nomearquivo,'w')
i=0
for container in containers :
    titulo = container.h2.a.text

    horario = container.span.text

    f.write('Titulo:' + titulo + '\n' + horario + '\n' + '-------------------------------' + '\n')
    if i == 15:
        print(type(titulo))
        print(type(horario))


    print(titulo)
    print(horario)
    print(i)
    i+=1

f.close()




