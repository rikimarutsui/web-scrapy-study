from pymongo import MongoClient
from datetime import datetime
import json

class MongoConnector:
	def __init__(mysillyobject, host, dbname, collectionname):
		host = 'mongo-scrapy'
		dbname = 'webscrapy'

		mysillyobject.client = MongoClient(host, 27017)
		print('Mongo Database connected!')

		mysillyobject.db = mysillyobject.client[dbname]
		mysillyobject.collection = mysillyobject.db[collectionname]
		print(mysillyobject.collection)

	def countDocuments(mysillyobject, in_json):
		return mysillyobject.collection.count_documents(in_json)

	def insertOne(mysillyobject, in_json):
		return mysillyobject.collection.insert_one(in_json).inserted_id

	def insertMany(mysillyobject, in_jsonarr):
		return mysillyobject.collection.insert_many(in_jsonarr).inserted_ids

	def findOne(mysillyobject, in_json):
		return mysillyobject.collection.find_one(in_json)

	def find(mysillyobject, in_json):
		return mysillyobject.collection.find(in_json)


