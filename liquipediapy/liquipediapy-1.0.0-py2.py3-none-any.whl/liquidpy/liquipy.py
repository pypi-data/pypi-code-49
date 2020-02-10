import exceptions
from bs4 import BeautifulSoup
import requests


class liquipy():
	def __init__(self,appname):
		self.__headers = {'User-Agent': appname,'Accept-Encoding': 'gzip'}
		self.__base_url = 'https://liquipedia.net/dota2/api.php?'

	def parse(page,page_format='json'):
		url = self.__base_url+'action=parse&format='+page_format+'&page='+page
		response = requests.get(url, headers=self.__headers)
		if response.status_code == 200:
			try:
				page_html = response.json()['parse']['text']['*']
			except KeyError:
				raise exceptions.RequestsException(response.json(),response.status_code)	
			soup = BeautifulSoup(page_html,features="lxml")
			redirect = soup.find('ul',class_="redirectText")
			if redirect is None:
				return soup,None
			else:
				redirect_value = soup.find('a').get_text()
				redirect_value = quote(redirect_value)
				url = self.__base_url+'page='+redirect_value
				soup,__ = self.__get_parsed_html(url)
				return soup,url
		else:
			raise exceptions.RequestsException(response.json(),response.status_code)	


	def search(serach_value,page_format='json'):
		url = self.__base_url+'action=opensearch&format='+page_format+'&search='+serach_value
		response = requests.get(url, headers=self.__headers)
		if response.status_code == 200:
			return  response.json()
		else:
			raise exceptions.RequestsException(response.json(),response.status_code)		