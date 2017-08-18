import requests
from bs4 import BeautifulSoup
page=requests.get('https://en.wikipedia.org/wiki/Google')
soup=BeautifulSoup(page.content,'html.parser')
a=""
for paragraph in soup.find_all('p'):
    a=a+str(paragraph.text)
for text in a.split('.'):
    print(text)