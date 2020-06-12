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

from lxml import etree

html = etree.HTML(html_doc)

print('選擇節點（selecting nodes）')
print(html.xpath('/html'))
print(html.xpath('/html/body/a'))
print(html.xpath('//a'))
print(html.xpath('/html/body//a'))
print(html.xpath('//a/@href'))

print('判斷式（predicates）')
print(html.xpath('/html/body//a[1]'))
print(html.xpath('/html/body//a[last() - 1]'))
print(html.xpath('/html/body//a[position() < 3]'))
print(html.xpath('//p[@class]'))
print(html.xpath('//p[@class="title"]'))