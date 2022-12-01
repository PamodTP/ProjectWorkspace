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

#search_string = 'driverless OR "self driving" -is:retweet'
search_string = '((driverless) OR "self driving" OR selfdriving OR "self-driving") (law OR legislation OR rules OR ban OR allow OR legal OR standard) -is:retweet -is:reply'

tweets = api.search_recent_tweets(search_string)
# next_tweets = api.search_recent_tweets(query="driverless OR self driving -is:retweet", next_token=next_page)

total_message_list=[]
counter=0
#repeat search for subsequent pages
while tweets.meta.get("next_token"):
    page_message_list = tweets.data
    total_message_list.append(page_message_list)
    next_page = tweets.meta.get("next_token")
    tweets = api.search_recent_tweets(query=search_string, next_token=next_page)
    #adding limit to ensure requests stay within limit with flexibility for reruns/testing
    counter=counter+1
    if counter==500:
        break

    
json_data = []
for page in total_message_list:
    for message in page:
        json_data.append(message.text)

with open('tweets.json', 'w') as json_file:
    json.dump(json_data, json_file) 

 
# Writing to data.txt
# with open("data.txt", "a", encoding='utf-8') as outfile:
#     for page in total_message_list:
#         for message in page:
#             outfile.write(message.text)
#             outfile.write('!NEWTWEET-HERE!')


    

pass
# print(total_message_list)