import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS

url = 'https://es.stackoverflow.com/users/'
usuario = raw_input("Ingrese Usuario: ")
url = url + str(usuario) + "?tab=tags"
pagina = requests.get(url)

sopa = BeautifulSoup(pagina.content, 'html.parser')
user = sopa.find_all('a',class_='post-tag')

nombres = list()
for i in user:
    nombres.append(i.text)
print(nombres)

with open('nube.txt','w+') as file:
    file.write(str(nombres))

stopwords =[]

abrir = open('nube.txt','r+')
data = abrir.read().replace('','')

nube = WordCloud(width=700,height=700,background_color='cyan',stopwords=stopwords,min_font_size=20, max_font_size=400).generate(data)

nube.to_file('Nube.png')
print('Imagen Generada')
print('Imagen Guardada')

#Universidad de Guayaquil
#Proyecto Procesos de Software
#Integrantes
#Joel Andres Villao De la S