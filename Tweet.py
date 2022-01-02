import os 
import tweepy
from dotenv import load_dotenv
import time

load_dotenv()
# Consumer keys and access tokens, used for OAuth
consumer_key= os.getenv('CONSUMER_KEY')
consumer_secret=os.getenv('CONSUMER_SECRET')
access_token=os.getenv('ACCESS_TOKEN')
access_token_secret='ACCESS_TOKEN_SECRET'

# OAuth process, using the keys and tokens

auth = os.getenv('AUTH')
os.getenv('ACCESS_TOKEN_SECRET')


# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
user = api.get_user("twitter")

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)

for follower in limit_handler.tweepy.cursor(api.followers).items():
    if follower.name =='':
        follower.follow()
    print(follower.name)