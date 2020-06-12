import requests
from bs4 import BeautifulSoup

html_doc = requests.get('http://www.hko.gov.hk').text
soup = BeautifulSoup(html_doc, 'lxml')

print(soup.prettify())
