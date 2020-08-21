import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS

usuario = raw_input('Ingrese Usuario:') # Ingrese usuario por numero de ID
url = 'https://es.stackoverflow.com/users/' + str(usuario) + '?tab=tags'
pagina = requests.get(url)

leer = BeautifulSoup(pagina.content, 'html.parser')
filtro = leer.find_all('a',class_='post-tag')

tags = list()
for i in filtro:
    tags.append(i.text)
print(tags)

with open('nube.txt','w+') as file:
    file.write(str(tags))

stopwords =[]

abrir = open('nube.txt','r+')
etiquetas = abrir.read().replace('','')

nube = WordCloud(width=700,height=700,background_color='cyan',stopwords=stopwords,min_font_size=20, max_font_size=400).generate(etiquetas)

nube.to_file('Nube.png')
print('Imagen Generada')
print('Imagen Guardada')

nube.to_file("/content/img.png")
img=nube.to_image()
img

#Universidad de Guayaquil
#Proyecto Procesos de Software
#Integrantes
#Joel Andres Villao De la S
#Ivan harijan Ramos Ochoa
#Jonathan Andy Quimis M2Endoza
#Victor Hugo Varas Roca
