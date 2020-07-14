import requests


html = requests.get('http://www.wikipedia.org')
print(html.read())