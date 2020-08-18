import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS

url = 'https://es.stackoverflow.com/users/'
usuario = input('Ingrese un Usuario: ')
url = url + str(usuario) + '?tab=tags'
pagina = requests.get(url)

sopa = BeautifulSoup(pagina.content, 'html.parser')

user = sopa.find_all('a', class_='post-tag')

nombres = list()

for i in user:
    nombres.append(i.text)
print(nombres)

numeros = sopa.find_all('span', class_='item-multiplier-count')
numero = list()

for i in numeros:
    numero.append(i.text)
print(numero)

with open('nube.txt', 'w')as file:
    file.write(str(nombres))

comment_words = ''
stopwords = ['k', "'", """'"""]

abrir = open('nube.txt', 'r+')
data = abrir.read().replace('\n', '')

wordcloud = Wordcloud (width=700, height=700, background_color='white',stopwords=stopwords, min_fon_size=10, max_words=300).generate(data)

wordcloud.to_file('image.png')
print('imagen guardada')

