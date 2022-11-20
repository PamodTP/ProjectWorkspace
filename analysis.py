import nltk
#example
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer

#example following https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk#step-6-preparing-data-for-the-model
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')

tokenizer = TweetTokenizer(strip_handles=True)


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

tweet_tokens = tokenizer.tokenize(tweet_list)
s0 = "This is a cooool #dummysmiley: :-) :-P <3 and some arrows < > -> <--"
tokenizer.tokenize(s0)

# display list
print(tweet_list)