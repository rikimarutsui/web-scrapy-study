from pymongo import MongoClient

host = 'db-nosql-scrapy'
dbname = 'web-scrapy'

client = MongoClient(host, 
					 port=27017,
                     username='webscrapy',
                     password='password123')
print('Mongo Database connected!')

db = client[dbname]
mycol = db["web-scrapy-list"]
