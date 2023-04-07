import snscrape.modules.twitter as twitterScraper
import pandas as pd
from pymongo import MongoClient
import streamlit as st
from datetime import datetime

# create mongo db connection
client = MongoClient("localhost", 27017)
myMongoDB = client["master_scraper_db"]
myMongoCollection = myMongoDB["twitter_scrapper_data"]


def saveScrapDataToMongoDB(json_result):
    myMongoCollection.insert_one(json_result)


# scrap_twitter_data - function accept a query parameter
def scrap_twitter_data(query):
    row_result = []
    for i, tweet in enumerate(
            twitterScraper.TwitterSearchScraper(query).get_items()):
        if i > tweet_count:
            break
        else:
            row_result.append([tweet.date, tweet.id, tweet.url, tweet.rawContent, tweet.user.username, tweet.replyCount,
                               tweet.retweetCount, tweet.lang, tweet.source,
                               tweet.likeCount])
            # print(tweet.rawContent)
    twitterData = pd.DataFrame(row_result, columns=["date", "id", "url", "tweet content", "user", "reply count",
                                                    "retweet count", "language", "source", "like count"])
    json_result = {"Scraped Word": query,
                   "Scraped Date": datetime.today(),
                   "Scraped Data": row_result
                   }

    saveScrapDataToMongoDB(json_result) # saving scrapped data into mongoDB
    return twitterData


# Set page title
st.set_page_config(page_title="Twitter Scraper")

# Add page title
st.title("Twitter Scraper")

# Add text input for keyword or hashtag
keyword = st.text_input("Enter a keyword or hashtag to search")

# Add date range selector
start_date = st.date_input("Start date")
end_date = st.date_input("End date")

# Add slider for tweet count limit
tweet_count = st.slider("Select tweet count limit", 0, 1000, 100)

# Add button to start scraping


if st.button("Scrape"):
    # Do the scraping here
    query = keyword + ' until:' + str(end_date) + ' since:' + str(start_date)
    showData = scrap_twitter_data(query)

    st.dataframe(showData)
