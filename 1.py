import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["mydatabase"]
mycol=mydb["customer"]

mydict={"name": "John","address": "Highway 37"}

x=mycol.insert_one(mydict)

y=mycol.find_one()

print(x)
