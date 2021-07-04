import tweepy
import time

# Consumer keys and access tokens, used for OAuth
consumer_key= 'LzJY9qc1oqkEKgQBAwCSDugjT'
consumer_secret='5JWAFz8Rg6FFnvfJ3t2oYSPGIxNg0tssLi7tHxmKVQrwQ7nLtb'
access_token='AAAAAAAAAAAAAAAAAAAAAFNRJgEAAAAAmsfoa%2BeONzYnBO8t45IlK4rQQyw%3DxBDUmr6K7ZnZ74sZVRdmdZmxM4HIVK08eMvFyxXiGqMxOi2k7I'
access_token_secret='cgGtzTncnsInV7c9VoEK847kPcyIa4mrqXtA6Jqp6xEvd9pPzM'

# OAuth process, using the keys and tokens

auth = tweepy.OAuthHandler('DOiw2oaXwB8UDclGAMiee6H9X', '9sbRspj1Nh3oIfrkz99eXxBFiqhKUeXrKpVMI27VAkIz0eYHv5')
auth.set_access_token('232197853-AYgxUgle67GWKoGNq2ijg782UF0HSI7oHVFLI43H','IhfgiNkRmQIcmkSLyIqhWAGZHRvKKqejKephxHKWgfIRP')


# Creation of the actual interface, using authentication
api = tweepy.API(auth, wait_on_rate_limit=True)
user = api.me()

def limit_handler(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

for follower in limit_handler.tweepy.cursor(api.followers).items():
    if follower.name =='':
        follower.follow()
    print(follower.name)