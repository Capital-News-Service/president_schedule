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
* Print json in console as string

#### Version 3
* Turn string into dataframe
* Search for "MD" in either details, location, or url by iterating over rows
* If found, print out event in console

* Hardcode words
  - Gaylord
  - James J. Rowley Training
  - Camp David
  - Walter Reed
  - Hagerstown
  
  - Aberdeen Proving Ground
  - Fort Meade
  - NSA (be more specific)
  - https://en.wikipedia.org/wiki/List_of_federal_installations_in_Maryland