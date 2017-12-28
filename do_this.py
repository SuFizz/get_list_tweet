import tweepy
consumer_key = "get this key"
consumer_secret =  "get this secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)
all_rts = api.retweets(946444606769639424)
f = open("all_rts.txt", 'a')

for tweet in all_rts:
    f.write(tweet.user.screen_name)
f.close()
