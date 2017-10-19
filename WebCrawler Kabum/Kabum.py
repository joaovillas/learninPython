from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import xlwt

my_url =input('URL:')
my_url = my_url.replace(' ','')+'?ordem=5&limite=100&pagina=1&string='
file_name = input('File Name:')
file_name = file_name.replace(' ','_')+'.csv'


uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,'html.parser')
containers = page_soup.findAll('div',{'class':'listagem-box'})

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(u'nome da placa')


#inicializando cabeçalhos
worksheet.write (0,0,'Nome')
worksheet.write (0,1,'Preço a vista')
worksheet.write (0,2,'Preço parcelado')
worksheet.write (0,3,'Preço com desconto')
i=1

#Loop pra escrever documentação no excel
for container in containers :
    nomedaplaca = container.span.text
   


    preco = container.findAll('div',{'class':'listagem-precoavista'})
    preco_avista = preco[0].b.text
    


    preco = container.findAll('div',{'class':'listagem-preco12x'})
    preco_12x = preco[0].text.replace('OU','')
    
    
    preco = container.findAll('div',{'class':'listagem-preco'})
    precodesconto = preco[0].text
    preco = container.findAll('div',{'class':'H-15desc'})
    precodesconto = precodesconto +" "+preco[0].text
    

    worksheet.write (i,0,nomedaplaca)
    worksheet.write (i,1,preco_avista)
    worksheet.write (i,2,preco_12x)
    worksheet.write (i,3,precodesconto)
    i=i+1

print('------------------------------ ARQUIVO CRIADO COM SUCESSO ------------------------------')

workbook.save(file_name)