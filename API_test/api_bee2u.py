import requests


url = ("https://elasticsearch-saps.saude.gov.br/leitos-uf/_search?pretty")
s = requests.get(url)
s.json()
print(s)