
from distutils.log import error
from twitter_part import config_setup
from tweepy import errors
while True:
    
    try:
        default = config_setup()

        default.create_twitter_obj()


        tweets = default.find_user_tweets("YeenaJust")
        print(tweets)
        for x in tweets:
            print(x.id_str,'-   ',x.full_text)
            
            replies = default.find_replies(f'{x.id_str}','YeenaJust',100)
            if replies == None:
                print("No replies")
            else:
                for y in replies:
                    print(f"replied: {y.user.screen_name}  {y.text}  ")
    except:
        print("Подожди немного")



