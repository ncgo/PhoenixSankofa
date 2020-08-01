from flask import Flask, jsonify, request, Response, render_template
from pykafka import KafkaClient
import json

def get_kafka_client():
  return KafkaClient(hosts='127.0.0.1:9092')

app = Flask(__name__)

@app.route('/')
def index():
  return('LEAFLET MAP')

if __name__ == "__main__":
  app.run(debug=True, port=5001)

 
