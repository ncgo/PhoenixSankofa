import tweepy

CONSUMER_KEY = "HLLexVYTwMPO2yEOc1TpF1Z9k"
CONSUMER_SECRET = "I6Lo7UaikQHXJvpNVptIMUyWk9OZc23On212EHoO4f4alQ0e7A"
ACCESS_KEY = "1289832546906394624-IGeD6CArrjtH89yNU5Pbh1WZ8RH4HM"
ACCESS_SECRET = "tl0KKkCrOVAGfIEMZvGqYxkhZv3TSXFx3NA2nTrVl1XrK"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
