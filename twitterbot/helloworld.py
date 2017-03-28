#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'aiyXooRQRNxWCOKP8cXC5zNO5'
CONSUMER_SECRET = 'ZhQifwowGocGvrPr4nABL6oo89bB5ZZrW57zDJf0M83spwlT86'
ACCESS_KEY = '368169901-EdClXnc12uzsL0nZbWQuNOtEDeBJ7UZyGdXn4AhL'
ACCESS_SECRET = '2YVtcLaAYaXnnh5OEt8MlB8jyvWBr2zXNF0JvZmzs47NO'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    api.update_status(line)
    time.sleep(60)#Tweet every 15 minutes
