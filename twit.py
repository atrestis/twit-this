import tweepy
from mycreds import *



auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)
api.update_status('Update your status from here :)')

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
    

#results = api.search("NYTAD")
#for tweet in results:
  #  print(tweet.text)
