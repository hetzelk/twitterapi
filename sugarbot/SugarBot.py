import tweepy
from keys import keys
class TwitterBot(object):

    def __init__(self):
        self.argfile = str("lines.txt")
        
        
        CONSUMER_KEY = keys['consumer_key']
        CONSUMER_KEY_SECRET = keys['consumer_secret']
        ACCESS_TOKEN = keys['access_token']
        ACCESS_TOKEN_SECRET = keys['access_token_secret']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
        auth.secure = True
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)

        
     

    def tweet(self):

        filename=open(self.argfile,'r')
        f=filename.readlines()
        filename.close()
        
        for line in f:
            self.api.update_status(status = line)




twit = TwitterBot()
twit.tweet()
            
