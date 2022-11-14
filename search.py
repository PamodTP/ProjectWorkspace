#from https://towardsdatascience.com/how-to-extract-data-from-the-twitter-api-using-python-b6fbd7129a33
import requests
import os
import json
import tweepy
from dotenv import load_dotenv

consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]

api = tweepy.Client(bearer_token, consumer_key, consumer_secret, \
        access_token, access_token_secret)

tweets = api.search_recent_tweets("driverless")

print(tweets)