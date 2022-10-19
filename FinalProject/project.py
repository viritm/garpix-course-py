import requests
import mimetypes
from bs4 import BeautifulSoup

sourceLink = "https://stopgame.ru/news/all/p1"
imgDirPath = "./Data/Imgs"


def getFilePath(index, ext):
    return f'{imgDirPath}/image_{index}{ext}'


r = requests.get(sourceLink)

soup = BeautifulSoup(r.text, 'html.parser')

links = [data['src'] for data in soup.findAll('img')]

for index, link in enumerate(links):
    r = requests.get(link)
    content_type = r.headers['content-type']
    ext = mimetypes.guess_extension(content_type) or '.jpg'
    path = getFilePath(index, ext)
    with open(path, mode='wb') as f:
        f.write(r.content)


print(links)
