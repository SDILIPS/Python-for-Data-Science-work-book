import tweepy 
from textblob import TextBlob

consumerKey = '4lPXzlNfC2ZP9oKLFL0R2eQP8'
consumerSecret = 'HPktFzlVHnu3ppSYBwZFcwPnr8b0tp25StjjIjskeVPyykiaBK'

accessToken = '76032279-HREDBimLDIHOmBvaKO0ZLgzaJNLRPj9UIcEjWIvS8'
accessTokenSecret = 'bXgeAvB21S6AgG4mnWga7XXau7ylsVRQ89NwJeKJlTkv8'

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
	print(tweet.text);
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)

