import requests
url = f'https://random-word-api.herokuapp.com/word?number=10'
r = requests.get(url)
print(r.text)