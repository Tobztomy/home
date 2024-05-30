import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo3"]
mycol=mydb["employee"]

for x in mycol.find({},{"_id":0,"name":1,"address":1}):
    print(x)