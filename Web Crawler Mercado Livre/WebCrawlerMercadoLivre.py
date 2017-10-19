from urllib.request import urlopen as uReq  
from bs4 import BeautifulSoup as soup 
import xlwt


my_url = input('URL:')
my_url = my_url.replace(' ','')
filename = input('File name:')
filename = filename.replace(' ','_')

filename = filename +'.csv'

#abrindo conexão com a página 
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,'html.parser')
containers = page_soup.findAll('div',{'class':'item__info'})


workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(u'nome da placa')

#inicializando cabeçalhos
worksheet.write (0,0,'Nome')
worksheet.write (0,1,'Preço a vista')

i=1

for container in containers :
    
    nome_placa = container.h2.span.text
    
    preco_container = container.findAll('span',{'class':'price-fraction'})
    preco = preco_container[0].text
    preco = 'R$ '+preco.strip()
    worksheet.write(i,0,nome_placa)
    worksheet.write(i,1,preco)
    i+=1

workbook.save(filename)




