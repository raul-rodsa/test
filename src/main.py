import requests

def curl(url):
	r = requests.get(url)
	
	return r.content
print(curl("https://www.google.es"))
