import tweepy, time, sys, os, random
from keys import keys
from datetime import datetime, timedelta
from random import randint
class TwitterBot(object):

    def __init__(self):
        self.argfile = str("lines.txt")
        self.trumpFile = str("trump.txt")
        self.tweetlist = []
        self.favlist = [] 

        CONSUMER_KEY = keys['consumerkey']
        CONSUMER_KEY_SECRET = keys['consumerkeysecret']
        ACCESS_TOKEN = keys['accesstoken']
        ACCESS_TOKEN_SECRET = keys['accesstokensecret']
        auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_KEY_SECRET)
        auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        self.api = tweepy.API(auth)
        self.tweetlist = []
        self.favlist = []   

    def tweet(self):
        print('tweetFunction')
        filename=open(self.argfile,'r')
        f=filename.readlines()
        filename.close()
        
        line = random.choice (f)
        try:   
            self.api.update_status(status = line)
            sleepTime = randint(120,360)
            time.sleep(sleepTime)
        except Exception as e:
            print(e)
            twit.main()

    def tweetSearchedTerm(self):
        print('tweetSearchTerm')
        query = self.api.search(q="bald is beautiful",count = 50)
        try:
            for tweet in query:
                    screenName = tweet.user.screen_name
                    message = "@%s BALD IS BEAUTIFUL" %(screenName)
                    result = self.api.update_status(status = message)

                    sleepTime = randint(120,360)
                    time.sleep(sleepTime)
        except Exception as e:
            print(e)
            twit.main()
                       

    def trendingTweet(self):
        print('trendingTweet')
        
        trendingTopics = self.api.trends_place(id=2379574)
        hashtags = [item['name'] for item in trendingTopics[0]['trends'] if item['name'].startswith('#')]
        print(hashtags)
        

        trendHashtag = hashtags[randint(0, len(hashtags)-1)]
        tweetSearchResults = self.api.search(q=trendHashtag, count=2)

        filename=open(self.argfile,'r')
        randomTerms=filename.readlines()
        filename.close()
        
        try:
            for tweet in tweetSearchResults:
                screenName = tweet.user.screen_name
                message = randomTerms[randint(0, len(randomTerms)-1)]
                
                
                tweetMessage ="@{0}, {1} {2}".format(screenName, message, trendHashtag)
                print (message)
                status = self.api.update_status(status=tweetMessage, in_reply_to_status_id = tweet.id)

                sleepTime = randint(120,360)
                time.sleep(sleepTime)
        except Exception as e:
            print(e)
            

        functionSleepTime = randint(3600,4000)
        time.sleep(functionSleepTime)
    

    def tweetDonaldTrump(self):
        print('TRUMP TIME!!!')
        filename=open(self.trumpFile,'r')
        trumpTime=filename.readlines()
        filename.close()

        try:
            message = trumpTime[randint(0, len(trumpTime)-1)]
            tweet = "@realDonaldTrump, {0}".format(message)
            path ='C:/Users/rcisneros_be/Documents/twitterapi/sugarbot/images'
            image = (path + '/' + random.choice(os.listdir(path)))
            filename = path+image
            result = self.api.update_with_media(image,status=tweet)

            sleepTime = randint(120,360)
            time.sleep(sleepTime)
       
        except Exception as e:
            print(e)
            twit.main()
            
    def follow (self):
        for follower in tweepy.Cursor(self.api.followers).items():
            try:
                follower.follow()
                print(follower.screen_name)
            except Exception as e:
                print(e)
                twit.main()

    def retweet(self):
        #retweetsearchQuery = str(input("Enter searchterm for retweet. "))
        for result in self.api.search(q="bald", lang="en"):
            self.tweetlist.append(result.id)
        try:
            numTweets = len(self.tweetlist)
            
            rand = random.randint(0, numTweets)
            self.api.retweet(self.tweetlist[rand])
            
        except Exception as e:
            print(e)
            twit.main()

    def favorite(self):
        #favsearchQuery = str(input("Enter searchterm for favorite. "))
        for result in self.api.search(q="toupee", lang="en"):
            self.tweetlist.append(result.id)
        try:
            numTweets = len(self.tweetlist)
            rand = random.randint(0, numTweets)
            self.api.create_favorite(self.tweetlist[rand])

        except Exception as e:
            print(e)
            twit.favorite()
    

    
        
    def main(self):

        randomNum= randint(0,70)
        if randomNum <=10:
            twit.tweet()
        elif 10 < randomNum <=20:
            twit.tweetDonaldTrump()
        elif 20< randomNum <=30:
            twit.trendingTweet()
        elif 30< randomNum <=40:
            twit.tweetSearchedTerm()
        elif 40< randomNum <=50:
            twit.follow()
        elif 50< randomNum <=60:
            twit.retweet
        elif 60< randonNum <=70:
            twit.favorite()
        twit.main()
        


twit = TwitterBot()
twit.main()
            
