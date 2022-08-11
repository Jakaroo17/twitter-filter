import config as cfg
import tweepy


def config_setup():
    return TwitterObj(cfg.BEARER_TOKEN,cfg.CONSUMER_API_KEY,
    cfg.CONSUMER_API_KEY_SECRET,cfg.ACCESS_TOKEN,cfg.ACCESS_TOKEN_SECRET)

class TwitterObj:
    def __init__(self,bearer_token,
                consumer_key,consumer_secret,
                acces_token,acces_token_secret):
        self._bearer_token = bearer_token
        self._consumer_key = consumer_key
        self._consumer_key_secret = consumer_secret
        self._access_token = acces_token
        self._access_token_secret = acces_token_secret

    def create_twitter_obj(self):
        self._client = tweepy.Client(bearer_token=self._bearer_token,
        consumer_key=self._consumer_key, consumer_secret=self._consumer_key_secret,
        access_token=self._access_token,access_token_secret=self._access_token_secret)

        self._auth = tweepy.OAuth1UserHandler(
        consumer_key=self._consumer_key, consumer_secret=self._consumer_key_secret,
        access_token=self._access_token,access_token_secret=self._access_token_secret)

        self._api = tweepy.API(auth=self._auth)          

    def find_user_tweets(self,name,count = 100):
        tweets = self._api.user_timeline(screen_name=name, 
                           count=count+2,
                           include_rts = False,
                           tweet_mode = 'extended'
                           )
        return tweets
    
    def find_replies(self,tweet_id,items):
       replies=[]
       for tweet in tweepy.Cursor(self._api.search_tweets,q='to:'+self.username).items(items):
            if hasattr(tweet, 'in_reply_to_status_id_str'):
                if (tweet.in_reply_to_status_id_str==tweet_id):
                    replies.append(tweet)
       if(not replies): return None
       return replies

    def disable_eveything_from_user(self,reply_id,user_id):
        self._client.block(user_id)
        self._client.mute(user_id)
        self._client.hide_reply(reply_id)
    
    def set_username(self,username):
        self.username = username

      




# # client.delete_tweet(id=1550908991513006083)
# # client.mute()
# # client.hide_reply(id=1549745844638949376)
# test.client.block()
# test.client.hide_reply()
# test.client.mute()

