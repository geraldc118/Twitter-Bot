import tweepy
import time

# Consumer keys and access tokens, used for OAuth
consumer_key= 'SBDD2qGrPZubCnLToGxbfgVNM'
consumer_secret='vmaXdxD9UtXQDp8rqYoIiD0q5YGjYH1njU6ekmhbuD2y1F4GnS'
access_token='232197853-EqMHejWYy0hyqY3TPGFSFObgb2dMI5WIBBKL7XG9'
access_token_secret='Kl4osyhn2eHAw11tbaLRfWDCw8vNmZ1RqphXKSGGaeS9d'

# OAuth process, using the keys and tokens

auth = tweepy.OAuthHandler("SBDD2qGrPZubCnLToGxbfgVNM", "vmaXdxD9UtXQDp8rqYoIiD0q5YGjYH1njU6ekmhbuD2y1F4GnS")
auth.set_access_token("232197853-EqMHejWYy0hyqY3TPGFSFObgb2dMI5WIBBKL7XG9","Kl4osyhn2eHAw11tbaLRfWDCw8vNmZ1RqphXKSGGaeS9d")


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