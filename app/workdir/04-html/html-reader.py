html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
</body></html>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'lxml')

print('type(soup):')
print(type(soup)) # get the soup object

print('soup.prettify():')
print(soup.prettify()) # get the html prettify

print('soup.head:')
print(soup.head) # get the head tag

print('soup.head.title:')
print(soup.head.title) # get the title

print('soup.a:')
print(soup.a) # get the first a tag

print('soup.body.contents:')
print(soup.body.contents) # get the body contents

print('soup.a.parent:')
print(soup.a.parent) # get the first a tag parent

print('soup.a.next_sibling:')
print(soup.a.next_sibling) # get the element of same level of the first a tag

print('soup.find_all(b):')
print(soup.find_all('b')) # search b tag

print('tag.name:')
import re
for tag in soup.find_all(re.compile("^b")): # search all tag name is start with 'b'
    print(tag.name)

print('soup.find_all(a,b):')
print(soup.find_all(['a', 'b'])) # search tag a and b


def has_class_no_id(tag): # function
    return tag.has_attr('class') and not tag.has_attr('id')

print('has_class_no_id:')
print(soup.find_all(has_class_no_id));

print('soup.html.find_all(title):') # find all title
print(soup.html.find_all("title"))

print('soup.html.find_all(title, recursive=False):') 
print(soup.html.find_all("title", recursive=False)) # only search title tag name in html

print('soup.find_all(id=link2)')
print(soup.find_all(id='link2')) # 找出 id 屬性值為 link2 的標籤

print('soup.find_all(href=re.compile(elsie))') 
print(soup.find_all(href=re.compile("elsie"))) # 用 re 找出 href 屬性值包含 elsie 的標籤

print('soup.find_all(id=True)')
print(soup.find_all(id=True)) # 找出有 id 屬性的標籤


print('soup.find_all(href=re.compile(elsie), id=link1)')
print(soup.find_all(href=re.compile("elsie"), id='link1'))# 也可以同時使用多個屬性來判斷


