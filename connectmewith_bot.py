import tweepy
import time

print("Connect Me With by Team Phoenix Sankofa for Twitter Hackathon")

CONSUMER_KEY = "RFGhccptD6bbBwtuzcmqinsro"
CONSUMER_SECRET = "vX5Vm4liCTmYqVL3cSdBhc2e6k7RpdNOl874ElXVaxnjbBcqup"
ACCESS_KEY = "1289353192568958981-C3MN1FsmmUTt0LF5DQRct1REnxzSjq"
ACCESS_SECRET = "yQoNOzSuaAXvnt1K1VgtVtJQwi1At28qGxCmE7E1AlBB8"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

# dictionary keeping track of users who tweet at the bot
# ex. 0: [id1, id2]
matching_dict = {}

# only looks at new tweets


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return


# analyses tweets


def reply_to_tweets_and_match():
    print("retrieving tweets...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)

    mentions = api.mentions_timeline(last_seen_id)
    for mention in reversed(mentions):
        print(str(mention.id) + " - " + mention.text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        words = mention.text.lower().split(" ")

        # prints the mentions words
        print(words)

        # set up for matching:
        if len(matching_dict.keys()) == 0:
            match = 0

        # looks for BLM topic

        if "blm" in words or "blacklivesmatter" in words:
            if (
                match not in matching_dict.keys()
            ):  # add the first user that requested blm and responds
                matching_dict[match] = [mention.user.id]
                print("responding back...", flush=True)
                api.update_status(
                    "@" + mention.user.screen_name + " Preparing your connection...",
                    mention.id,
                )
                print("update sent!", flush=True)
            elif (
                len(matching_dict[match]) == 1
            ):  # add the other user and prepare to add a new entry
                matching_dict[match].append(mention.user.id)
                api.update_status(
                    "@" + mention.user.screen_name + "You have been connected!",
                    mention.id,
                )
                match += 1
                # call the direct message/ text with those user

        print(matching_dict)


# loops every 15sec

while True:
    reply_to_tweets_and_match()
    time.sleep(15)
