## President Schedule

**Problem:** It is difficult to know when the president is visiting Maryland or if he's meeting with a Maryland member or a Maryland company.
**Solution:** Search the president’s public calendar for anything Maryland related.

#### Version 1
Sends out a tweet when the program runs to a Twitter account.
* Create a gmail account for bot
  - presidentschedulemd@gmail.com
* Create a Twitter account using gmail account
  - @president_s_md
* Get keys for Twitter account at apps.twitter.com
* Create GitHub repo with 4 files: pstutorial.md, pskey.json, readme.md, GitIgnore, & pscode.py
* Write the following code in pskey.json:
  - consumer key, consumer key secret, access token, & access token secret
* Write the following code in pscode.py:
  - Import Json & Tweepy
  - Call in authentication information from pskey.json
  - Store them so they can be passed into Twitter
  - Create keyword to tweet out
  - Tweet out keyword with authentication to test
```
import json
import tweepy

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
tweet = "president schedule"
buildTweet(tweet)

def buildTweet(argument1):
    tweet = "president schedule"
    sendTweet(tweet)

def sendTweet(content):
    try:
        api.update_status(content)
    except tweepy.error.TweepError:
        pass
```

#### Version 2 
Print out in console the President's entire schedule in office as json
* Visit https://factba.se
  - Go to President Donald Trump
  - Go to Topics
  - Click President's Public Calendar
  - Download json at https://factba.se/rss/calendar-full.json
* In pscode.py import json
* Print json in console as list of dictionaries
* Turn list of dictionaries into dataframe
```
import requests
import pandas as pd

#import president's schedule as json
url_schedule = 'https://factba.se/rss/calendar-full.json'
get_schedule = requests.get(url_schedule)
json_schedule = get_schedule.json()
print(json_schedule)

scedule_df = pd.DataFrame(json_schedule)
```

#### Version 3
* Iterate over colums location and details to find list of words below
* If found, print out event in console

* Visited
  - MD
  - Gaylord
  - James J. Rowley
  - Camp David
  - Walter Reed
  - Hagerstown
  - Joint Base Andrews
* Not yet visited
  - Aberdeen
  - Fort Meade
  - Fort Detrick
  - Naval Academy
```
import numpy as np

mdgov = ["MD", "Gaylord", "James J. Rowley", "Camp David", "Walter Reed", "Hagerstown", "Joint Base Andrews", "Aberdeen", "Fort Meade", "Fort Detrick", "Naval Academey"]
    
for m in mdgov:
	scheduledf = scheduledf.replace(np.nan, '', regex=True)
    mdsearch = scheduledf[scheduledf['details'].str.contains(m) | scheduledf['location'].str.contains(m)]
    if (len(mdsearch) > 0):
        irow = mdsearch.iterrows()
        for i in irow:
            print(i[1]['location'])
```
  
#### Version 4
* Get today's date
* Search for date in data frame
* For that day, search for list of words below in either details or location by iterating over rows
* If found, print out event in console
```
import datetime

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

mdgov = ["MD", "Gaylord", "James J. Rowley", "Camp David", "Walter Reed", "Hagerstown", "Joint Base Andrews", "Aberdeen", "Fort Meade", "Fort Detrick", "Naval Academey"]  
for m in mdgov:
    mdsearch = psdate[psdate['details'].str.contains(m) | psdate['location'].str.contains(m)]
    if (len(mdsearch) > 0):
        irow = mdsearch.iterrows()
        for i in irow:
            print("President in MD")
```

#### Version 5
* For current day, if there is one event with a keyword, print date
* Eliminate repeat dates so eac date is only printed once
* Format tweet the president is visitng on date
