# -*- coding: utf-8 -*-
from twitter_config import config
import twitter # https://python-twitter.readthedocs.io

class Twitter:
    api = twitter.Api(consumer_key=config['consumer_key'],
                      consumer_secret=config['consumer_secret'],
                      access_token_key=config['access_token_key'],
                      access_token_secret=config['access_token_secret'])

class NewPost(Twitter):
    @classmethod
    def __init__(self, text):
        self.api.PostUpdate(text)

class UserPosts(Twitter):
    message_list = []
         
    def __init__(self, username):
        self.username = username
        self.user_message_col = self.api.GetUser(screen_name=self.username)
        self.get_stack_messages()

    def get_stack_messages(self, start_id=None):
        messages = self.api.GetUserTimeline(screen_name=self.username, count=200, max_id=start_id)
        self.message_list += messages
        self.return_stack_messages()

    def return_stack_messages(self):
        for record in self.message_list:
            print(record.created_at)
            print(record.text, '\n')
            