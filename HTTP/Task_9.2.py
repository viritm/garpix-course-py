import requests

myUrl = "https://www.ozon.ru/search/?from_global=@&sorting=@&text=@"

myParams = ["true", "price", "d3*"]


def getDataFromUrl(url, myParams):
    actualUrl = ""
    myParams.reverse()

    for el in url:
        if el == '@':
            actualUrl += myParams.pop()
        else:
            actualUrl += el

    r = requests.get(actualUrl)

    return f'URL : {actualUrl}\nStatus code : {r.status_code}\n'


print(getDataFromUrl(myUrl, myParams))
