import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo2"]
mycol=mydb["employee"]

myquery={"address":"Park Lane 38"}

mydoc=mycol.find(myquery)

for x in mydoc:
    print(x)