import snscrape.modules.twitter as twitterScraper
import streamlit as st

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

st.write(twitterData)
# Set page title
st.set_page_config(page_title="Twitter Scraper")

# Add page title
st.title("Twitter Scraper")

# Add dropdown
options = ["Keyword", "Hashtag"]
selected_option = st.selectbox("Search by", options)

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
    query = keyword + ' until:' + end_date + ' since:' + start_date
    st.write(query)
    twitterScraper.TwitterSearchScraper(query).get_items()
    # query = 'dataScientist until:2023-04-06 since:2023-04-05'
    st.write(
        f"Scraping {selected_option} {tweet_count} tweets with keyword/hashtag '{keyword}' from {start_date} to {end_date}")
