import requests
from bs4 import BeautifulSoup

url = "https://www.neoteo.com/enlaces-recomendados-de-la-semana-n689/"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
f=open("test.txt","w")
contador=1
for link in soup.find_all('a'):
    data=str(link.get("href")).strip()
    f.write(str(contador)+"-"+str(link.text).strip()+": ")
    f.write(data)
    f.write("\n")
    contador+=1
    
f.close()
    