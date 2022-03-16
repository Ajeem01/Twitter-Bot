import tweepy
import time

auth = tweepy.OAuthHandler('KGdaVjzyl2oxQtycmvc221Y7b', 'L9ruOo2ODbvHge7Lt1MtJBDAlwPNXNuxpc1wFu4N8ppwVqkpVh')
auth.set_access_token('1481895749470519298-wxM1n6Sk6yUsMbSywHJjlfyuzkmfrP', 'BNcqXCT6vNIJpCNlObV6Ni5sJRMnVGKPMWNMQrs7MAkQa')

api = tweepy.API(auth)
user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'kda'
numbersOfTweets = 2

for tweet in tweepy.Cursor(api.search, search_string).items(numbersOfTweets):
    try: 
        tweet.favorite()
        print("I liked that tweet")
    except tweepy.TweepError as err:
        print(err.reason)
    except StopIteration:
        break    



