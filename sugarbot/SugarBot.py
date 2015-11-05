import tweepy
from keys import keys
class TwitterBot(object):

    def __init__(self):
        self.argfile = str("lines.txt")
        
        
        CONSUMER_KEY = keys['consumerkey']
        CONSUMER_KEY_SECRET = keys['consumerkeysecret']
        ACCESS_TOKEN = keys['accesstoken']
        ACCESS_TOKEN_SECRET = keys['accesstokensecret']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
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
            