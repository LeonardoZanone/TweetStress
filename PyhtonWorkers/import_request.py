import requests

URL = "http://localhost:5000/estado/put"

data = {"Estado": "São Paulo", "Sentimento": "Positive"}

r = requests.put(url=URL, params=data)
