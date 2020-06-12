from pymongo import MongoClient
from datetime import datetime
import json

host = 'db-nosql-scrapy'
dbname = 'web-scrapy'

client = MongoClient(host, 27017)
print('Mongo Database connected!')

db = client[dbname]
print(db.collection_names)

