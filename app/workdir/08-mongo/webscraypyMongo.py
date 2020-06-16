from mongoConnector import MongoConnector
import requests
import re
from bs4 import BeautifulSoup

mc = MongoConnector('mongo-scrapy', 'webscrapy', 'collectInfo')

url = 'https://edition.cnn.com/world'
html_doc = requests.get(url).text
soup = BeautifulSoup(html_doc, 'lxml')

article_tags = soup.find_all('ul')

for article_tag in article_tags:
	cd_content_tag = article_tag.find('div', class_='cd__content')
    
	if cd_content_tag != None and cd_content_tag.a['href'][:1] == "/":
		newsTitle = cd_content_tag.find('span', class_='cd__headline-text').text
		newsLinkage = url + cd_content_tag.a['href']
		
		print("News Title: ", newsTitle)
		print("News Linkage: ", newsLinkage)
		newsJson = { 
			'news-title' : newsTitle, 
			'news-linkage' : newsLinkage 
		}
		mc.insertOne(newsJson)

