import nltk
import json
import string
import re
from nltk.corpus import stopwords
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer

stop_words = stopwords.words('english')
punctuation = string.punctuation


#example following https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk#step-6-preparing-data-for-the-model
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text_sample = twitter_samples.strings('tweets.20150430-223406.json')

tokenizer = TweetTokenizer(strip_handles=True)


#real
# Empty list to read list from a file
tweet_list = []
tweets_string = ''

# Open file and read the content in a list
# with open("data.txt", "r", encoding='utf-8') as infile:
#     for line in infile:
#         # Remove \n from end of each line
#         tweet = line[:-1]
#         # Input document separates tweets by a blankline
#         if tweet == '' :
#             tweet = '!NEWTWEET-DELIMITER!'
#         # Combine multiline tweets into one tweet. Use 'NEWTWEET' as delimiter. 
#         tweets_string = tweets_string + tweet

# tweet_list = tweets_string.split('!NEWTWEET-DELIMITER!')

tweets_file = open("tweets.json")
tweets = json.load(tweets_file)
tweets_file.close()

pattern = re.compile('https:(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
#pattern = re.compile('maga')


def process_tweet(text):
    """
    Function to process a single tweet

    Input: Single tweet string
    Output: Processed tweet string
    """
    # all lowercase
    text = text.lower()
    # remove hyperlinks
    text = pattern.sub('', text)
    # remove newline marker
    text = text.replace("\n", "")
    # remove punctuation
    text = "".join([char for char in text if char not in string.punctuation])
    
    return text


processed_tweet_list = []

for tweet in tweets:
    processed_tweet = process_tweet(tweet)
    processed_tweet_list.append(processed_tweet)



#tweet_tokens = tokenizer.tokenize(tweets)

print("x")



pass

