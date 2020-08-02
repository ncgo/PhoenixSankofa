from tinydb import TinyDB, Query
import random
from GoogleNews import GoogleNews

# setting up database
links_db = TinyDB("links.json")
Topic = Query()

# setting up google news api
googlenews = GoogleNews(lang="en")
googlenews.setperiod("3")


def return_random_link(topic):
    links = links_db.search(Topic.topic == topic)
    if len(links) == 0:
        # return the google news link
        print("fetching google link")
        googlenews.search(topic)
        google_links = googlenews.result()
        return google_links[0]["link"]
    else:
        print("fetching link from database")
        choice = random.randrange(0, len(links) - 1)
        return links[choice]["link"]


print(return_random_link("latinx"))
