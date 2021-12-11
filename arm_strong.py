import requests

url = "https://docs.github.com/en/rest/reference/repos"



resp = requests.get(url)
print(resp)