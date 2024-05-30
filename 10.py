import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo3"]
mycol=mydb["employee"]

x=mycol.delete_many({})

print(x.deleted_count,"document deleted")