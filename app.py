import streamlit as st

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
    st.write(f"Scraping {selected_option} {tweet_count} tweets with keyword/hashtag '{keyword}' from {start_date} to {end_date}")
