import requests
import re
from bs4 import BeautifulSoup

html_doc = requests.get('https://edition.cnn.com/world').text
soup = BeautifulSoup(html_doc, 'lxml')

article_tags = soup.find_all('ul')#, class_=re.compile("^cn cn-list cn-list-hierarchical-xs"))

for article_tag in article_tags:
    cd_content_tag = article_tag.find('div', class_='cd__content')
    
    if cd_content_tag != None and cd_content_tag.a['href'][:1] == "/":
        print("News Title: ", cd_content_tag.find('span', class_='cd__headline-text').text)
        print("News Linkage: ", cd_content_tag.a['href'])
