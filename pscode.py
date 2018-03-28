import json

#opens and reads mvkey.json
pskey={}
with open("keys/pskey.json") as file:
    pskey = json.loads(file.read())
    
# Consumer keys and access tokens, used for OAuth
consumer_key = pskey["consumer_key"]
consumer_secret = pskey["consumer_secret"]
access_token = pskey["access_token"]
access_token_secret = pskey["access_token_secret"]
    