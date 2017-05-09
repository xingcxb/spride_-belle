# -*- coding: utf-8 -*-

import requests
import json
import time
import os
from bs4 import BeautifulSoup

class belle():
	
	##先获得图片集合入口，然后单页读取图片
	def getpic_url(self):
		list_belle = []
		main_url = "http://www.beautylegmm.com"
		headers = {'user-agent' : 'easymbol-app/0.1'}
		html = requests.get(main_url,headers = headers)

		print("retnrn code = " + str(html.status_code))
		
		#获得首页图集
		#暂不支持翻页效果
		htmlmain = BeautifulSoup(html.text,"html.parser")
		belle_url = htmlmain.find_all(class_='post_weidaopic')
		for bellepage_url in belle_url:
			list_belle.append(bellepage_url.a['href'])
		
		#抓取，图集下面的数据
		#暂不支持翻页
		i = 0
		for url in list_belle:
			pic_html = requests.get(url,headers = headers)
			pic_info_html = BeautifulSoup(pic_html.text,"html.parser")
			picInfo_url = "http://www.beautylegmm.com"
			pic_list_url = pic_info_html.find_all('img')
			for pic_url in pic_list_url:
				print(pic_url)
				newurl = pic_url['src']
				if 'page' not in newurl:
					newurl = picInfo_url + newurl
					path_local = '/Users/symbol/Pictures/test'
					data = requests.get(newurl)
					fp = open(path_local + "/" + str(i) + ".jpg",'wb')
					fp.write(data.content)
					fp.close()
					i+=1

			print(pic_html.text)
			break


if __name__ == "__main__":
	belleurl = belle()
	belleurl.getpic_url()