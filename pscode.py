import json
import tweepy
import requests
import pandas as pd
import numpy as np

#opens and reads mvkey.json
pskey={}
with open("pskeys/pskey.json") as file:
    pskey = json.loads(file.read())
  
# Consumer keys and access tokens, used for OAuth
consumer_key = pskey["consumer_key"]
consumer_secret = pskey["consumer_secret"]
access_token = pskey["access_token"]
access_token_secret = pskey["access_token_secret"]

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Store access keys in a way to send to Twitter
api = tweepy.API(auth)

def buildTweet(argument1):
    tweet = "president schedule"
    sendTweet(tweet)

def sendTweet(content):
    try:
        api.update_status(content)
    except tweepy.error.TweepError:
        pass

#import president's schedule as json to dataframe
urlschedule = 'https://factba.se/rss/calendar-full.json'
importschedule = requests.get(urlschedule)
jsonschedule = importschedule.json()
schedule_df = pd.DataFrame(jsonschedule)


schedule_df



schedule_df = schedule_df.replace(np.nan, '', regex=True)    
md = schedule_df[schedule_df['details'].str.contains("MD")]
    
if (len(md) > 0):
    irow = md.iterrows()
    for i in irow:
        print(i[1]['details'])
        print(i[1]['date'])

