import snscrape.modules.twitter as twitterScraper
import json
import pandas as pd
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

myMongoDB = client["master_scraper_db"]
myMongoCollection = myMongoDB["twitter_scrapper_data"]

# scraper = twitterScraper.TwitterUserScraper("SrBachchan")
# twitterScraper.TwitterSearchScraper

# for i, tweet in enumerate(scraper.get_items()):

row_result = []
query = 'dataScientist until:2023-04-06 since:2023-04-05'
for i, tweet in enumerate(
        # twitterScraper.TwitterSearchScraper('#BipashaBasu since:2023-04-05 until:2023-04-06', top=True).get_items()):
        twitterScraper.TwitterSearchScraper(
            query).get_items()):
    if i > 5:
        break
    else:
        row_result.append([tweet.date, tweet.id, tweet.url, tweet.rawContent, tweet.user.username, tweet.replyCount,
                           tweet.retweetCount, tweet.lang, tweet.source,
                           tweet.likeCount])
        # print(tweet.rawContent)
twitterData = pd.DataFrame(row_result, columns=["date", "id", "url", "tweet content", "user", "reply count",
                                                "retweet count", "language", "source", "like count"])
# print(twitterData)


json_result = {"Scraped Word": query,
               "Scraped Date": "15022023",
               "Scraped Data": row_result
               }

# print(json_result)

file = open("twitter_scraper.json", "w")
jData = json.dumps(json_result, default=str)
file.write(jData)
file.close()

rec = myMongoCollection.insert_one(json_result)
print("Record inserted successfully ")
