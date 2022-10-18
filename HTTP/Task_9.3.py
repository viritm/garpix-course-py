import json
import requests

pls = ['python', 'c++', 'java', 'javascript', 'ruby', 'c#']


def grq(langs): return [[lang, json.loads(requests.get('https://api.github.com/search/repositories',
                                                       params={'q': f'languages:{lang}'}).text)["total_count"]] for lang in langs]


print(grq(pls))
