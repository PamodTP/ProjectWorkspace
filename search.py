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

tweets = api.search_recent_tweets('driverless OR "self driving" -is:retweet')
# next_tweets = api.search_recent_tweets(query="driverless OR self driving -is:retweet", next_token=next_page)

total_message_list=[]
counter=0
#repeat search for subsequent pages
while tweets.meta.get("next_token"):
    page_message_list = tweets.data
    total_message_list.append(page_message_list)
    next_page = tweets.meta.get("next_token")
    tweets = api.search_recent_tweets(query="driverless OR self driving -is:retweet", next_token=next_page)
    #adding limit to ensure requests stay within limit with flexibility for reruns/testing
    counter=counter+1
    if counter==100:
        break

 
# Writing to data.txt
with open("data.txt", "a", encoding='utf-8') as outfile:
    for page in total_message_list:
        for message in page:
            outfile.write(message.text)

print(total_message_list)