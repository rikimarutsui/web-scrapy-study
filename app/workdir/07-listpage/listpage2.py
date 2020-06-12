import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://ithelp.ithome.com.tw/articles?tab=tech').text
soup = BeautifulSoup(html_doc, 'lxml')

title_tags_1 = soup.select('html > body > div > div.row > div.col-md-12.clearfix > div.leftside > div.board.tabs-content > div.qa-list > div.qa-list__content > h3.qa-list__title > a.qa-list__title-link')
titles_1 = [tag.text for tag in title_tags_1]

title_tags_2 = soup.select('div.qa-list > div.qa-list__content > h3.qa-list__title > a.qa-list__title-link')
titles_2 = [tag.text for tag in title_tags_2]

title_tags_3 = soup.select('a.qa-list__title-link')
titles_3 = [tag.text for tag in title_tags_3]

print(titles_1 == titles_2 and titles_2 == titles_3)
