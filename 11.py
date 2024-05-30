import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo2"]
mycol=mydb["employee"]

myquery={"address":{"$regex":"^S"}}
newvalues={"$set":{"name":"Minnie"}}

x=mycol.update_many(myquery,newvalues)

print(x.modified_count,"document upadted")