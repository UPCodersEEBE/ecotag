import pymongo

client = pymongo.MongoClient("mongodb+srv://tampier:tampier@cluster0.wybmf.mongodb.net/ecotag?retryWrites=true&w=majority")

db = client.ecotag

objects = db.objects

eco_foot_step = {
    "id": 1,
    "name": "plastic bottle" ,
    }

objects.insert_one(eco_foot_step)







