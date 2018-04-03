import json
import tweepy
import requests
import pandas as pd
import numpy as np
import datetime

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
scheduledf = pd.DataFrame(jsonschedule)

#import today's date
def getDate():
    now = datetime.datetime.now()
    date = now.strftime('%Y-%m-%d')
    return date

#search for md locations only for today
date = getDate()
scheduledf = scheduledf.replace(np.nan, '', regex=True)
psdate = scheduledf[scheduledf['date'].str.contains(date)]
if (len(psdate) > 0):
    irow = psdate.iterrows()

#mdgov = ["MD", "Gaylord", "James J. Rowley", "Camp David", "Walter Reed", "Hagerstown", "Joint Base Andrews", "Aberdeen", "Fort Meade", "Fort Detrick", "Naval Academey"]
mdgov = ["Oval"]    
for m in mdgov:
    mdsearch = psdate[psdate['details'].str.contains(m) | psdate['location'].str.contains(m)]
    if (len(mdsearch) > 0):
        irow = mdsearch.iterrows()
        for i in irow:
            print("President in MD")
                    