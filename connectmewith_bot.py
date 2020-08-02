import tweepy
import time
import random
from tinydb import TinyDB, Query
from access import api
from direct_message import dm_article, dm_connection

print("Connect Me With by Team Phoenix Sankofa for Twitter Hackathon")

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
            id_list.append(entry["user_id"])

        print(id_list)
        print(mention.user.id in id_list)

        # looks for BLM topic

        if "blm" == words[1] or "blacklivesmatter" == words[1]:
            print("blm topic")
            if len(matching_db.search(Topic.topic == "blm")) == 0:
                # if there's only one user
                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "blm",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )
                print("responding back...", flush=True)

                # send them an article related to topic
                dm_article(mention.user.id, mention.user.screen_name, "blm")

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
            elif (
                mention.user.id not in id_list
            ):  # so it doesn't connect you with yourself
                print("match can be made!")
                # select a random user in the database before inserting this one:
                current_users_in_db = matching_db.search(Topic.topic == "blm")
                if len(matching_db.search(Topic.topic == "blm")) == 1:
                    user_to_connect_index = 0
                else:
                    user_to_connect_index = random.randrange(
                        0, len(current_users_in_db) - 1
                    )
                user_to_connect = current_users_in_db[user_to_connect_index]
                user_to_connect_id = user_to_connect["user_id"]
                user_to_connect_handle = user_to_connect["handle"]

                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "blm",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )

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

                print("\nsending articles!\n")
                dm_article(mention.user.id, mention.user.screen_name, "blm")
                print("\npairing users!\n")
                # dm this user about their connection
                dm_connection(mention.user.id, user_to_connect_handle)
                # dm the matched user
                dm_connection(user_to_connect_id, mention.user.screen_name)
                print("ready for a new match!")
        # looks for acc topic
        elif "acc" == words[1]:
            print("acc topic")
            if len(matching_db.search(Topic.topic == "acc")) == 0:
                # if there's only one user
                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "acc",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )
                print("responding back...", flush=True)

                # send them an article related to topic
                dm_article(mention.user.id, mention.user.screen_name, "acc")

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
            elif (
                mention.user.id not in id_list
            ):  # so it doesn't connect you with yourself
                print("match can be made!")
                # select a random user in the database before inserting this one:
                current_users_in_db = matching_db.search(Topic.topic == "acc")
                if len(matching_db.search(Topic.topic == "acc")) == 1:
                    user_to_connect_index = 0
                else:
                    user_to_connect_index = random.randrange(
                        0, len(current_users_in_db) - 1
                    )
                user_to_connect = current_users_in_db[user_to_connect_index]
                user_to_connect_id = user_to_connect["user_id"]
                user_to_connect_handle = user_to_connect["handle"]

                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "acc",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )

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

                print("\nsending articles!\n")
                dm_article(mention.user.id, mention.user.screen_name, "acc")
                print("\npairing users!\n")
                # dm this user about their connection
                dm_connection(mention.user.id, user_to_connect_handle)
                # dm the matched user
                dm_connection(user_to_connect_id, mention.user.screen_name)
                print("ready for a new match!")
        elif "feminism" == words[1]:
            print("feminism topic")
            if len(matching_db.search(Topic.topic == "feminism")) == 0:
                # if there's only one user
                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "feminism",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )
                print("responding back...", flush=True)

                # send them an article related to topic
                dm_article(mention.user.id, mention.user.screen_name, "feminism")

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
            elif (
                mention.user.id not in id_list
            ):  # so it doesn't connect you with yourself
                print("match can be made!")
                # select a random user in the database before inserting this one:
                current_users_in_db = matching_db.search(Topic.topic == "feminism")
                if len(matching_db.search(Topic.topic == "feminism")) == 1:
                    user_to_connect_index = 0
                else:
                    user_to_connect_index = random.randrange(
                        0, len(current_users_in_db) - 1
                    )
                user_to_connect = current_users_in_db[user_to_connect_index]
                user_to_connect_id = user_to_connect["user_id"]
                user_to_connect_handle = user_to_connect["handle"]

                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "feminism",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )

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

                print("\nsending articles!\n")
                dm_article(mention.user.id, mention.user.screen_name, "feminism")
                print("\npairing users!\n")
                # dm this user about their connection
                dm_connection(mention.user.id, user_to_connect_handle)
                # dm the matched user
                dm_connection(user_to_connect_id, mention.user.screen_name)
                print("ready for a new match!")
        elif "latinx" == words[1]:
            print("latinx topic")
            if len(matching_db.search(Topic.topic == "latinx")) == 0:
                # if there's only one user
                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "latinx",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )
                print("responding back...", flush=True)

                # send them an article related to topic
                dm_article(mention.user.id, mention.user.screen_name, "latinx")

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
            elif (
                mention.user.id not in id_list
            ):  # so it doesn't connect you with yourself
                print("match can be made!")
                # select a random user in the database before inserting this one:
                current_users_in_db = matching_db.search(Topic.topic == "latinx")
                if len(matching_db.search(Topic.topic == "latinx")) == 1:
                    user_to_connect_index = 0
                else:
                    user_to_connect_index = random.randrange(
                        0, len(current_users_in_db) - 1
                    )
                user_to_connect = current_users_in_db[user_to_connect_index]
                user_to_connect_id = user_to_connect["user_id"]
                user_to_connect_handle = user_to_connect["handle"]

                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": "latinx",
                        "open": 1,
                        "location": mention.user.location,
                    }
                )

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

                print("\nsending articles!\n")
                dm_article(mention.user.id, mention.user.screen_name, "latinx")
                print("\npairing users!\n")
                # dm this user about their connection
                dm_connection(mention.user.id, user_to_connect_handle)
                # dm the matched user
                dm_connection(user_to_connect_id, mention.user.screen_name)
                print("ready for a new match!")
        else:
            topic_submitted = words[1]
            print("custom topic: " + topic_submitted)
            if len(matching_db.search(Topic.topic == topic_submitted)) == 0:
                # if there's only one user
                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": topic_submitted,
                        "open": 1,
                        "location": mention.user.location,
                    }
                )
                print("responding back...", flush=True)

                # send them an article related to topic
                dm_article(mention.user.id, mention.user.screen_name, topic_submitted)

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
            elif (
                mention.user.id not in id_list
            ):  # so it doesn't connect you with yourself
                print("match can be made!")
                # select a random user in the database before inserting this one:
                current_users_in_db = matching_db.search(Topic.topic == topic_submitted)
                if len(matching_db.search(Topic.topic == topic_submitted)) == 1:
                    user_to_connect_index = 0
                else:
                    user_to_connect_index = random.randrange(
                        0, len(current_users_in_db) - 1
                    )
                user_to_connect = current_users_in_db[user_to_connect_index]
                user_to_connect_id = user_to_connect["user_id"]
                user_to_connect_handle = user_to_connect["handle"]

                matching_db.insert(
                    {
                        "name": mention.user.name,
                        "handle": mention.user.screen_name,
                        "user_id": mention.user.id_str,
                        "topic": topic_submitted,
                        "open": 1,
                        "location": mention.user.location,
                    }
                )

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

                print("\nsending articles!\n")
                dm_article(mention.user.id, mention.user.screen_name, topic_submitted)
                print("\npairing users!\n")
                # dm this user about their connection
                dm_connection(mention.user.id, user_to_connect_handle)
                # dm the matched user
                dm_connection(user_to_connect_id, mention.user.screen_name)
                print("ready for a new match!")

    print(matching_db.all())


# loops every 15sec

while True:
    reply_to_tweets_and_match()
    time.sleep(15)
