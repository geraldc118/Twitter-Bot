import tweepy
import time

auth = tweepy.OAuthHandler("SBDD2qGrPZubCnLToGxbfgVNM", "vmaXdxD9UtXQDp8rqYoIiD0q5YGjYH1njU6ekmhbuD2y1F4GnS")
auth.set_access_token("232197853-EqMHejWYy0hyqY3TPGFSFObgb2dMI5WIBBKL7XG9","Kl4osyhn2eHAw11tbaLRfWDCw8vNmZ1RqphXKSGGaeS9d")


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
        print ("I liked that tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break