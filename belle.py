# -*- coding: utf-8 -*-

import requests
import json
import time
from bs4 import BeautifulSoup

class belle():
	
	##先获得图片集合入口，然后单页读取图片
	def getpic_url(self):
		url = "http://www.beautylegmm.com"
		headers = {'user-agent' : 'easymbol-app/0.1'}
		html = requests.get(url,headers = headers)

		print("retnrn code = " + str(html.status_code))
		#print(html.text)
		htmlmain = BeautifulSoup(html.text,"html.parser")
		list_belle_url = htmlmain.find_all(class_='post_weidaopic')
		for belle_url in list_belle_url:
			print(belle_url.a['href'])


if __name__ == "__main__":
	belleurl = belle()
	belleurl.getpic_url()