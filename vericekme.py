import requests
from bs4 import BeautifulSoup

r = requests.get('http://127.0.0.1:5500/index.html')
source = BeautifulSoup(r.content,"lxml")

metin = str(source.find("p").text)
baslık = str(source.title.text)

file = open("veri.txt", "w")
file.write("Sayfa Basligi: ")
file.write(baslık)
file.write(" --- Sayfa Metini ")
file.write(metin)