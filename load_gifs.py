import requests
import config
from bs4 import BeautifulSoup as BS

r = requests.get(config.siteurl)
html = BS(r.content, 'html.parser')
items = html.select("article img")
gifs = []

for el in items:
    gifs.append(config.siteroot+el.get('src'))

for el in range(len(gifs)):
    img_data = requests.get(gifs[el]).content
    with open(f'images/cat{el}.gif','wb') as handler:
        handler.write(img_data)