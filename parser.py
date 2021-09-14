from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import datetime

def parse(group=0):

	URL = 'https://intime.tsu.ru'
	HEADERS = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.147'		
	}
	
	#1gr
	if group==972101:
		URL = 'https://intime.tsu.ru/schedule/group/42974d38-ffca-11eb-8169-005056bc249c?name=972101'	
	if group==972102:
		URL = 'https://intime.tsu.ru/schedule/group/42974d3c-ffca-11eb-8169-005056bc249c?name=972102'
	if group==972103:
		URL = 'https://intime.tsu.ru/schedule/group/48902a31-ffca-11eb-8169-005056bc249c?name=972103'
	if group == 972105:
		URL = 'https://intime.tsu.ru/schedule/group/4e0e15aa-0699-11ec-816a-005056bc249c?name=972105'
	#2gr
	if group == 972001:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5a96-ffca-11eb-8169-005056bc249c?name=972001'
	if group == 972002:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5aa4-ffca-11eb-8169-005056bc249c?name=972002'
	if group == 972005:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5a9d-ffca-11eb-8169-005056bc249c?name=972005'
	#3gr
	if group == 971901:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5a45-ffca-11eb-8169-005056bc249c?name=971901'
	if group == 971902:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5a50-ffca-11eb-8169-005056bc249c?name=971902'
	if group == 971905:
		URL = 'https://intime.tsu.ru/schedule/group/41afdb6e-0699-11ec-816a-005056bc249c?name=971905'
	#4gr
	if group == 971810:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5915-ffca-11eb-8169-005056bc249c?name=971810'
	if group == 971811:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f591d-ffca-11eb-8169-005056bc249c?name=971811'
	if group == 971812:
		URL = 'https://intime.tsu.ru/schedule/group/3c9f5925-ffca-11eb-8169-005056bc249c?name=971812'	
	
	session = HTMLSession()

	if group!=0:
		response = session.get(URL)
		response.html.render()
				
		soup = BeautifulSoup(response.html.html, 'lxml')
		items = soup.findAll(class_ = 'ant-col ant-col-4')		

		weekday = datetime.datetime.today().isoweekday()
		# print (weekday)

		# upper_limit = int((len(items) / 6) * weekday)
		# lower_limit = int((len(items) / 6) * weekday - 6)	

		items = items[6:]	


		subjects = []
		for i in range(0,7):
			subjects.append(items[weekday + i * 6])		

		schedule = []	
		for item in subjects:
		 	subj = item.find(class_ = 'lesson-title')
		 	if (subj != None):
		 		schedule.append(subj.get_text())		 		
		 	else:
		 		schedule.append(' ')


		# if item is None:
		# 	schedule.append(' ')
		# else:
		# 	schedule.append(item.get_text())
				

		# for subject in subjects:
		# 	print(subject["title"])

		# for item in items:
		# 	print(item.get_text())

		# print (len(items))



		# print (response.html.html)
		print (len(items))
		for subj in schedule:
			print (subj)

	else:
		print ('Please, enter correct group number')

# soup = BeautifulSoup(src, "lxml")

a = input()
a = int(a,10)

parse(a)