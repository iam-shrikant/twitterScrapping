from pymongo import MongoClient

from datetime import datetime

# create mongo db connection
client = MongoClient("localhost", 27017)
myMongoDB = client["master_scraper_db"]
myMongoCollection = myMongoDB["twitter_scrapper_data_dummy"]

json_result = {"Scraped Word": "Hello",
               "Scraped Date": datetime.today(),
               "Scraped Data": "How are you"
               }


myMongoCollection.insert_one(dict(json_result))