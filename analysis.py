import nltk
#example
from nltk.corpus import twitter_samples

positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')

#real
# Empty list to read list from a file
tweet_list = []
tweets_string = ''

# Open file and read the content in a list
with open("data.txt", "r", encoding='utf-8') as infile:
    for line in infile:
        # Remove \n from end of each line
        tweet = line[:-1]
        # Input document separates tweets by a blankline
        if tweet == '' :
            tweet = '!NEWTWEET-DELIMITER!'
        # Combine multiline tweets into one tweet. Use 'NEWTWEET' as delimiter. 
        tweets_string = tweets_string + tweet

tweet_list = tweets_string.split('!NEWTWEET-DELIMITER!')


# display list
print(tweet_list)