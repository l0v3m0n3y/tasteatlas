import requests
class Client():
	def __init__(self):
		self.headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36","x-requested-with": "XMLHttpRequest"}
		self.api="https://www.tasteatlas.com/api"
	def search_map(self):
		return requests.get(f"{self.api}/search/searchmap",headers=self.headers).json()
	def me_country_code(self):
		return  requests.get(f"{self.api}/v2/me/country-code",headers=self.headers).text