import tweepy
import time

auth = tweepy.OAuthHandler('mjIbmhvdsK6m30eW8gUwD0xVO', '3qNHYEQrWj7RCUa3B7d6qvl0wuSOIZfv9ZgRd1ejifUewcZGTb')
auth.set_access_token('232197853-4M7Wch563zK8BaKwLOCbQNjEu4mbqKtafwWcgqa0','4shfMmhixlh8EQUNz3WfGurmqpwa2GrG1wodkdNZ07Txv')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)


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