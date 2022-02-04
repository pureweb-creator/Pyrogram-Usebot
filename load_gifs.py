import requests
import config
from bs4 import BeautifulSoup as BS
import uuid

r = requests.get(config.siteurl)
html = BS(r.content, 'html.parser')
items = html.select("article img")
gifs = []

for el in items:
    gifs.append(config.siteroot+el.get('src'))

for el in range(len(gifs)):
    img_data = requests.get(gifs[el]).content
    file_name = str(uuid.uuid4().hex)
    with open(f'downloads/{file_name}.gif','wb') as handler:
        handler.write(img_data)