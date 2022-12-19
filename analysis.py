import nltk
import json
import string
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.corpus import twitter_samples
from nltk.tokenize import TweetTokenizer, RegexpTokenizer

from transformers import pipeline

stop_words = stopwords.words('english')
punctuation = string.punctuation



#example following https://www.digitalocean.com/community/tutorials/how-to-perform-sentiment-analysis-in-python-3-using-the-natural-language-toolkit-nltk#step-6-preparing-data-for-the-model
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text_sample = twitter_samples.strings('tweets.20150430-223406.json')

tokenizer = TweetTokenizer(strip_handles=True)
lemmatizer = WordNetLemmatizer()


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
    # tokenize
    text = tokenizer.tokenize(text)
    # remove stop words
    text = [word for word in text if word not in stop_words]
    
     
    return text


processed_tweet_list = []

for tweet in tweets:
    processed_tweet = process_tweet(tweet)
    processed_tweet_list.append(processed_tweet)



#tweet_tokens = tokenizer.tokenize(tweets)

# cv = CountVectorizer()
# train_data = cv.fit_transform(tweets)
# data_shape = train_data.shape

# MNB = MultinomialNB()

model_path = f"cardiffnlp/twitter-roberta-base-sentiment-latest"

sentiment_pipeline = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

# Basic Testing Data
basic_data = ["I love you", "I hate you", "I like cars", "I dislike cars", "cars make me so sad man"]
model_output = sentiment_pipeline(basic_data)
model_results = {basic_data[i]: model_output[i] for i in range(len(basic_data))}

# Real Twitter Data
#model_output = sentiment_pipeline(tweets)
#print(output)

#model_results = {tweets[i]: model_output[i] for i in range(len(tweets))}

for entry in model_results:
    print(entry)
    print(model_results.get(entry))
    print('\n')

#continue following https://huggingface.co/blog/sentiment-analysis-python#3-building-your-own-sentiment-analysis-model
x = '6'


pass

