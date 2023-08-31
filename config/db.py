from pymongo import MongoClient
MONGO_URI = "mongodb://127.0.0.1:27017/CloudBoxPython"

conn = MongoClient(MONGO_URI)
