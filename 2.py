import pymongo
myclient=pymongo.MongoClient("mongodb://localhost/")
mydb=myclient["demo2"]
mycol=mydb["employee"]

mylist=[
{"name": "Amy","address": "Apple st 652"},
{"name": "Hannah","address": "Mountain 21"},
{"name": "Michael","address": "Valley 345"},
{"name": "Sandy","address": "Ocean blvd 2"},
{"name": "Betty","address": "Green Grass 1"},
{"name": "Richard","address": "Sky st 331"},
{"name": "Susan","address": "One way 98"},
{"name": "Vicky","address": "Yellow Garden 2"},
{"name": "Ben","address": "Park Lane 38"},
{"name": "William","address": "Central st 954"},
{"name": "Chuck","address": "Main Road 989"},
{"name": "Viola","address": "Sideway 1633"},
]
x=mycol.insert_many(mylist)

