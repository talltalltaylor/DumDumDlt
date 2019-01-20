# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 10:32:37 2019

@author: Taylor Robbins
"""
import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

keyword = "ENTER YOUR KEYWORD HERE!"

tweets = api.user_timeline(count=200)

for tweet in tweets:
    if keyword in tweet.text:
        api.destroy_status(id = tweet.id)
        
####Check to see if tweet is gone        
for tweet in tweets:
    print(tweet.text)
