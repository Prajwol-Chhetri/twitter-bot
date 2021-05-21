import tweepy
import time

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
user = api.me() 

def limit_handler(cursor):
	try:
		while True:
			yield cursor.next()  # cursor is a generator object so retrieving followers name
	except tweepy.RateLimitError:
		time.sleep(300)  # if ratelimiterror encountered wait for 1 second


search_string = ''  #enter your desired string to be searched here
numberOfTweets = 2

# using api search method searching for keyword 2 times and looping through it
for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
	try:
		tweet.favorite()  # liking the tweet containing search string
		tweet.retweet()  # retweeting the tweet containing search string
		print('I liked that tweet')
	except tweepy.TweepError as e:
		print(e.reason) # for each error printing the reason 
	except StopIteration:
		break  # breaking the loop if stop iteration occurs 