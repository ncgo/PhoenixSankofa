import tweepy
import time
from tinydb import TinyDB, Query

print("Connect Me With by Team Phoenix Sankofa for Twitter Hackathon")

CONSUMER_KEY = "RFGhccptD6bbBwtuzcmqinsro"
CONSUMER_SECRET = "vX5Vm4liCTmYqVL3cSdBhc2e6k7RpdNOl874ElXVaxnjbBcqup"
ACCESS_KEY = "1289353192568958981-C3MN1FsmmUTt0LF5DQRct1REnxzSjq"
ACCESS_SECRET = "yQoNOzSuaAXvnt1K1VgtVtJQwi1At28qGxCmE7E1AlBB8"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.txt"

# setting up database
matching_db = TinyDB("db.json")
Topic = Query()

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
        print(str(mention.id) + " - " + mention.text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        words = mention.text.lower().split(" ")

        # prints the mentions words
        print(words)

        # stores the user ids currently in db in list to check for duplicate tweets
        id_list = []
        for entry in matching_db.search(Topic.topic == "blm"):
            id_list.append(entry["id"])

        print(id_list)
        print(mention.user.id in id_list)

        # looks for BLM topic

        if "blm" in words[1] or "blacklivesmatter" in words[1]:
            matching_db.insert({"topic": "blm", "id": mention.user.id})
            if (
                len(matching_db.search(Topic.topic == "blm")) == 1
            ):  # if there's only one user
                print("responding back...", flush=True)

                # try-except to avoid duplicate error
                try:
                    api.update_status(
                        "@"
                        + mention.user.screen_name
                        + " Preparing your connection...",
                        mention.id,
                    )
                except tweepy.TweepError as error:
                    if error.api_code == 187:
                        # Do something special
                        print("\n\nduplicate message\n\n")
                    else:
                        raise error
                print("update sent!", flush=True)
            elif mention.user.id in id_list:  # so it doesn't connect you with yourself
                continue
                continue
            else:
                print("match made!")
                matching_db.insert({"topic": "blm", "id": mention.user.id})

                # try-except to avoid duplicate error
                try:
                    api.update_status(
                        "@" + mention.user.screen_name + " You have been connected!",
                        mention.id,
                    )
                except tweepy.TweepError as error:
                    if error.api_code == 187:
                        # Do something special
                        print("\n\nduplicate message\n\n")
                    else:
                        raise error

                print("preparing for a new match!")
            # call the direct message/ text with those user

        print(matching_db.all())


# loops every 15sec

while True:
    reply_to_tweets_and_match()
    time.sleep(15)
