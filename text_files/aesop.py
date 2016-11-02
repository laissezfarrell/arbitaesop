#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys, random

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = ''#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = ''#keep the quotes, replace this with your access token
ACCESS_SECRET = ''#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#tweet the random line
def tweet_line():
    def random_selection(): #select a random line
        filename = open(argfile).read().splitlines()
        f = random.choice(filename)
        return f;
    api.update_status(status=random_selection()) 
    return;

tweet_line()
    
count = 0
while count <= 1500:
    tweet_line()
    count = count + 1
    time.sleep(600)#Tweet every 10 minutes
