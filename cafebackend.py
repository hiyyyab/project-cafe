from flask import Flask, render_template
from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://hiyabgebreegziabher_db_user:uQwhvJqSkbgCAYw6@cafe-db.ugzmv2z.mongodb.net/?appName=cafe-db"
client = MongoClient(MONGODB_URI)

db = client["stars"]
collection = db["cafe-rating"]

app = Flask(__name__)
# data = [
#     {
#         "name": "Coffee Connection",
#         "rating": 4.7,
#         "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/WCkWhKTVOQGS6dOMIkSKiA/o.jpg"
#     },
#     {
#         "name": "Cafe BT",
#         "rating": 4.5,
#         "image_url": "https://s3-media0.fl.yelpcdn.com/bphoto/pPAE2JEtD4B40zIxLlooFQ/348s.jpg"
#
#     },
#     {
#         "name": "Starbucks",
#         "rating": 3.1,
#         "image_url" : "https://s3-media0.fl.yelpcdn.com/bphoto/mNVCAD9fjje36i1H8aj8_w/o.jpg"
#     }
# ]

@app.route("/")
def start_index():
    return render_template("index.html")


@app.route("/welcome")
def welcome():
    return "<html><body><h1><em>welcome</em></h1></body></html>"


@app.route("/search/<rating>")
def search_cafes(rating):
    rating = float(rating)
    result = []
    for cafe in collection.find():
        if cafe['rating'] >= rating:
            cafe["_id"] = str(cafe["_id"])
            result.append(cafe)
            print(result)
    return result


app.run(host="0.0.0.0", port=8000)
