import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me() 

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next() # cursor is a generator object so retrieving followers name
	except tweepy.RateLimitError:
		time.sleep(1000) # if ratelimiterror encountered wait for 1 second

for follower in limit_handler(tweepy.Cursor(api.followers).items()): # items because we want to loop through cursors
	name = ''  #enter the name of the follower you want to follow
	if follower.name == name:
		follower.follow()
		break
	else:
		print(f.'No follower named {name}')