import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), 'config.env')
load_dotenv(dotenv_path)

CONSUMER_API_KEY = os.getenv("TWITTER_CONSUMER_API_KEY")
CONSUMER_API_KEY_SECRET = os.getenv("TWITTER_CONSUMER_API_KEY_SECRET")
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")
ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
CLIENT_ID = os.getenv("TWITTER_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITTER_CLIENT_SECRET")

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
ADMIN_HASH = os.getenv("ADMIN_HASH")




