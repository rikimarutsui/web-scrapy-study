import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://ithelp.ithome.com.tw/articles?tab=tech').text
soup = BeautifulSoup(html_doc, 'lxml')

# 先找到文章區塊
article_tags = soup.find_all('div', class_='qa-list')

for article_tag in article_tags:
    # 再由每個區塊去找文章連結
    title_tag = article_tag.find('a', class_='qa-list__title-link')
    print(title_tag.text)