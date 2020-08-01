import tweepy
import time

print('Connect Me With by Team Phoenix Sankofa for Twitter Hackathon')

CONSUMER_KEY = 'RFGhccptD6bbBwtuzcmqinsro'
CONSUMER_SECRET = 'vX5Vm4liCTmYqVL3cSdBhc2e6k7RpdNOl874ElXVaxnjbBcqup'
ACCESS_KEY = '1289353192568958981-C3MN1FsmmUTt0LF5DQRct1REnxzSjq'
ACCESS_SECRET = 'yQoNOzSuaAXvnt1K1VgtVtJQwi1At28qGxCmE7E1AlBB8'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'

#only looks at new tweets

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

#analyses tweets

def reply_to_tweets():
    print('retrieving tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)

#looks for any topic

        print(mention.full_text.split(" ", 2)[1])

#looks for BLM topic

        if 'blm' in mention.full_text.lower().split(" ", 2)[1] or 'blacklivesmatter' in mention.full_text.lower().split(" ", 2)[1]:
        	print('responding back...', flush=True)
        	api.update_status('@' + mention.user.screen_name + ' Preparing your connection...', mention.id)
        	print('update sent!', flush=True)

#loops every 15sec

while True:
    reply_to_tweets()
    time.sleep(15)
