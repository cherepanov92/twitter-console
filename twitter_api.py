# -*- coding: utf-8 -*-
from twitter_config import config
import twitter # https://python-twitter.readthedocs.io

class Twitter:
    api = twitter.Api(consumer_key=config['consumer_key'],
                      consumer_secret=config['consumer_secret'],
                      access_token_key=config['access_token_key'],
                      access_token_secret=config['access_token_secret'])