#This is just a side thing. I want to visualize the tweets coming in
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler 
from tweepy import Stream
import access
from pykafka import KafkaClient
import json

def get_kafka_client():
  return KafkaClient(hosts='127.0.0.1:9092')

class StdOutListener(StreamListener):
  def on_data(self, data):
    print(data)
    message = json.loads(data)
    if message['place'] is not None: #only with geolocation on show messages on map
      client = get_kafka_client()
      topic = client.topics['twitterdata']
      producer = topic.get_sync_producer()
      producer.produce(data.encode('ascii'))
    return True

  def on_error(self, status_code):
    print(status_code)
    

if __name__ == "__main__":
  auth = OAuthHandler(access.CONSUMER_KEY, access.CONSUMER_SECRET)
  auth.set_access_token(access.ACCESS_KEY, access.ACCESS_SECRET)
  listener = StdOutListener()
  stream = Stream(auth, listener)
  stream.filter(track=['black lives matter'])