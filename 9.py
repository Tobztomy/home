import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo3"]
mycol=mydb["employee"]

mydoc=mycol.find().sort("name",-1)

for x in mydoc:
    print(x)