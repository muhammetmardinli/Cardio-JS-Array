import requests
from bs4 import BeautifulSoup

response = requests.get('https://en.wikipedia.org/wiki/Category:Boulevards_in_Paris')


soup = BeautifulSoup(response.content, 'html.parser')

boulevard_links = soup.select('#mw-pages .mw-category-group a')
boulevards = [link.text for link in boulevard_links]
newList = []
for i in boulevards :
    if "de" in i :
        newList.append(i)
for i in boulevards :
    print('"'+i+'"'+",")
