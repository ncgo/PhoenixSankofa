from access import api
from links import return_random_link
import tweepy

# dm link to user with article
def dm_article(user_id, user_handle, topic):
    link = return_random_link(topic)
    # api.send_direct_message(user_id, "Hey, here's an article you might like!\n" + link)
    try:
        api.send_direct_message(
            user_id,
            "Hey "
            + user_handle
            + "! Here's some news related to "
            + topic
            + "!\n"
            + link,
        )

    except tweepy.TweepError as error:
        if error.api_code == 349:
            print("user not following... responding")
            api.update_status(
                "@"
                + user_handle
                + " Please follow this account and try again so we can connect you via DMs!",
                user_id,
            )
            api.create_friendship(user_id)
        else:
            print("something went wrong :(")


# dm user that they've been connected to another user\
def dm_connection(user_id, connected_user_handle):
    api.send_direct_message(
        user_id,
        "Hey! You and @"
        + connected_user_handle
        + " have shared similar interests! Hit them up and talk about your passions! Use one of the articles we sent as a conversation starter!",
    )

