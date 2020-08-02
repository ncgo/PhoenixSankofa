import tweepy 

print('this is my twitter bot')

CONSUMER_KEY = 'RFGhccptD6bbBwtuzcmqinsro'
CONSUMER_SECRET = 'vX5Vm4liCTmYqVL3cSdBhc2e6k7RpdNOl874ElXVaxnjbBcqup'
ACCESS_KEY = '1289353192568958981-C3MN1FsmmUTt0LF5DQRct1REnxzSjq'
ACCESS_SECRET = 'yQoNOzSuaAXvnt1K1VgtVtJQwi1At28qGxCmE7E1AlBB8'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


