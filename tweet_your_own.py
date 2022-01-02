import os 
import tweepy
from dotenv import load_dotenv
import time

load_dotenv()

auth = os.getenv('AUTH')
os.getenv('ACCESS_TOKEN_SECRET')


api = tweepy.API(auth)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


search_string = 'IOTA'
numberoftweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numberoftweets):
    try:
        tweet.favorite()#changable for retweet ect
        print ("I liked that tweet")#changeable for anything else.
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break