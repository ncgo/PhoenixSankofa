from secrets import (
    API_KEY,
    API_SECRET_KEY,
    BEARER_TOKEN,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

import tweepy

# authorization set up for tweepy
auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# dictionary keeping track of users who tweet at the bot
# ex. 0: [id1, id2]
matching_dict = {}

#! for testing purposes using my personal account
def match_user():
    if len(matching_dict.keys()) == 0:
        match = 0
    last_seen_id = 1263920754858442752
    mentions = api.mentions_timeline(last_seen_id)
    for mention in reversed(mentions):
        print(mention.text)
        words = mention.text.split(" ")
        if words[0] == "@adirar111":  # if it contains some word
            if match not in matching_dict.keys():  # add the first user
                matching_dict[match] = [mention.user.id]
            elif (
                len(matching_dict[match]) == 1
            ):  # add the other user and prepare to add a new entry
                matching_dict[match].append(mention.user.id)
                match += 1
                # call the direct message/ text with those users

    print(matching_dict)


match_user()
