import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"


def mongo_connect(url):
    try: 
        conn = pymongo.MongoClient(url)
        print("Mongo is connect!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect("ENTER MONGODB ATLAS URL BEFORE RUNNING")

coll = conn["myTestDB"]["myFirstMDB"]

coll.remove({'first': 'douglas'})

documents = coll.find()

for doc in documents:
    print(doc)