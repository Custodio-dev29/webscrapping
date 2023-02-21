import requests
from bs4 import BeautifulSoup



#pagina que vamos trabalhar
url ='https://www.historicosblaze.com/blaze/doubles'

headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')
cores = soup.find_all('div', class_='double-single double-single-exporter border')



with open ('cores.csv','a',newline='',encoding='UTF-8') as f:
        for cor in cores:
                item = cor.find('span',class_='color-table').get_text()
                numero = cor.find('span',class_='number-table').get_text()
                minutos = cor.find('span',class_='minute-table').get_text()

                linha = item+"  " +numero+"  "+minutos+"\n"
                print(linha)
                f.write(linha)

                









