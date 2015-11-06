import tweepy, os, random, time
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
        self.tweetlist = []
        self.favlist = []     
     
    def tweet(self):

        filename=open(self.argfile,'r')
        f=filename.readlines()
        filename.close()
        
        for line in f:
            self.api.update_status(status = line)


    def follow (self):
        for follower in tweepy.Cursor(self.api.followers).items():
            follower.follow()
            print(follower.screen_name)


            
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
            twit.retweet()

        


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

        os.system("cls")

        twit = TwitterBot()
        twit.follow()
        counter = 0

        limit = int(input("How many times do you want to repeat? ")) 

        while counter <= (limit - 1):
            
            counter += 1
            print("")
            print("You just followed, favorited, tweeted, or retweeted,", counter, "time/s.")
            twit = TwitterBot()
            #twit.tweet()
            twit.favorite()
            twit.retweet()

            num = random.randint(120, 240)
            time.sleep(num)


twit = TwitterBot()
twit.main()			
	
