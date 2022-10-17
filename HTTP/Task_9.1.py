import requests


def getStatusCode(url):
    r = requests.get(url)
    return f'Status code is {r.status_code}\nURL : {url}'


print(getStatusCode("https://www.google.ru/"))
