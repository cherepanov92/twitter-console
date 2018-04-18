# -*- coding: utf-8 -*-
from twitter_config import config
import twitter # https://python-twitter.readthedocs.io

class Twitter:
    api = twitter.Api(consumer_key=config['consumer_key'],
                      consumer_secret=config['consumer_secret'],
                      access_token_key=config['access_token_key'],
                      access_token_secret=config['access_token_secret'])

class NewPost(Twitter):
    def __init__(self, text):
        self.api.PostUpdate(text)

class UserPosts(Twitter):
    post_count = 1
    message_list = []

    def __init__(self, username):
        self.username = username
        self.user_message_col = self.api.GetUser(screen_name=self.username).statuses_count

    def get_posts(self, start_id=None):
        messages = self.api.GetUserTimeline(screen_name=self.username, count=50, max_id=start_id)

        for message in messages:
            self.message_list.append(dict(id=self.post_count, date=message.created_at, text=message.text, message_id=message.id))
            self.post_count += 1

        return self.message_list