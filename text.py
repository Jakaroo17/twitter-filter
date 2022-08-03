import tweepy
import config as cfg

# userid = '1152103613847822336'

# tweets = api.user_timeline(user_id = userid, count = 200, include_rts = False)
# client.delete_tweet(id=1550908991513006083)
# client.get_rep
# client.mute()


# client.hide_reply(id=1549745844638949376)


# Считать реплаи к определенному твиту


client = tweepy.Client(bearer_token=cfg.BEARER_TOKEN,
consumer_key=cfg.CONSUMER_API_KEY, consumer_secret=cfg.CONSUMER_API_KEY,
access_token=cfg.ACCESS_TOKEN,access_token_secret=cfg.ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(consumer_key=cfg.CONSUMER_API_KEY,
consumer_secret=cfg.CONSUMER_API_KEY_SECRET,
access_token=cfg.ACCESS_TOKEN, access_token_secret= cfg.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth=auth)

# Считать твиты у пользователя
name = "YeenaJust"
tweets = api.user_timeline(screen_name=name, 
                           # 200 is the maximum allowed count
                           count=100,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

for info in tweets:
    print("ID: {}".format(info.id))
    print(info.created_at)
    print(info.full_text)
    print("\n")

# name = 'YeenaJust'
# tweet_id = '1533661183940694017'
# replies=[]
# for tweet in tweepy.Cursor(api.search_tweets,q='to:'+name).items(100):
#     if hasattr(tweet, 'in_reply_to_status_id_str'):
#         if (tweet.in_reply_to_status_id_str==tweet_id):
#             replies.append(tweet)

# for x in replies:
#     print(x.user.screen_name,'- ',x.text)

