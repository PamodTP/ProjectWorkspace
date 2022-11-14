import requests
import os
import json
import tweepy
import time
from dotenv import load_dotenv

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]

# api = tweepy.Client(bearer_token, consumer_key, consumer_secret, \
#         access_token, access_token_secret)

#initialise stream

stream = tweepy.StreamingClient(bearer_token)

#setup rules for stream
find_driverless = tweepy.StreamRule(value = "driverless -is:retweet")
find_self_driving = tweepy.StreamRule(value = "self driving -is:retweet")

stream.add_rules(add=[find_driverless, find_self_driving])

print(stream.get_rules())

#access stream
tweets = stream.filter()

#output streamed tweets to file for use
print(tweets)
# Serializing json
json_object = json.dumps(tweets, indent=4)
 
# Writing to sample.json
with open("streamed_tweets.json", "a") as outfile:
    outfile.write(json_object)

#close stream
time.sleep(5000)
stream.disconnect()