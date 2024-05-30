import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo3"]
mycol=mydb["employee"]

myquery={"address":{"$regex":"^S"}}

mydoc=mycol.find(myquery)

for x in mydoc:
    print(x)
