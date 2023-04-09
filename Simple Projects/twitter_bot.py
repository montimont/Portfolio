import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
auth.set_access_token("access_token", "access_token_secret")

# Create API object
api = tweepy.API(auth)

# Search for tweets related to Python, Javascript, and Machine Learning research
query = 'Python OR Javascript OR "Machine Learning" research'
tweets = api.search_tweets(query)

# Retweet and like the top 5 tweets
for tweet in tweets[:5]:
    api.retweet(tweet.id)
    api.create_favorite(tweet.id)

# Tweet a new message
message = 'Check out this article on Python research! #python #research'
api.update_status(message)