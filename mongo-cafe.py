

from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://hiyabgebreegziabher_db_user:uQwhvJqSkbgCAYw6@cafe-db.ugzmv2z.mongodb.net/?appName=cafe-db"
client = MongoClient(MONGODB_URI)

db = client["stars"]
collection = db["cafe-rating"]

# --- WRITE (insert one document) ---

collection.insert_one({"name": "Coffee Connection", "rating": 4.7, "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/WCkWhKTVOQGS6dOMIkSKiA/o.jpg"})
collection.insert_one({"name": "Cafe BT", "rating": 4.5, "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/pPAE2JEtD4B40zIxLlooFQ/348s.jpg"})
collection.insert_one({"name": "Starbucks", "rating": 3.1, "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/mNVCAD9fjje36i1H8aj8_w/o.jpg"})


# --- READ (find one document) ---
for f in collection.find():
    print(f)