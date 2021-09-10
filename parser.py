from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

def parse():
	URL = 'https://intime.tsu.ru/schedule/group/3c9f5a45-ffca-11eb-8169-005056bc249c?name=971901'
	# URL = 'https://intime.tsu.ru'
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.147'		
	}

	session = HTMLSession()

	response = session.get(URL)
	response.html.render(timeout=500)
	
	# response_rendered = get_intime()
	# response.html.render()
	# response = requests.get(URL, headers = HEADERS)
	# soup = BeautifulSoup(response.content, 'html.parser')
	# items = response.html.find('ant-col ant-col-4')

	# subjects = []

	# for item in items:
	# 	subjects.append({
	# 		'title': item.find('span', class_ = 'ant-tag ant-tag-orange').find('span', class_ = 'lesson-title').get_text(strip = True)
	# 	})

	# for subject in subjects:
	# 	print(subject["title"])

	# for item in items:
	# 	print(item.get_text())

	# print (len(items))

	print (response.html.html)
	# print (response_rendered.text)

# soup = BeautifulSoup(src, "lxml")

parse()