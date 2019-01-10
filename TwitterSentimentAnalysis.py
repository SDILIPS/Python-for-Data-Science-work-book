import tweepy 
from textblob import TextBlob

consumerKey = 'XYZ'
consumerSecret = 'XYZ'

accessToken = 'XYZ'
accessTokenSecret = 'XYZ'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text);
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

