# -*- coding: utf-8 -*-
from twitter_api import NewPost, UserPosts
from db_agent import DataBase

def run_command(method):
    def command_pagination(self, text):
        while True:
            try:
                user_input = str(input(text))
            except KeyboardInterrupt:
                print('Cancel')
                break
            else:
                print('Success')
                return method(self, user_input)
    return command_pagination

class CommandNewPost:

    def label(self):
        return 'New post'

    def perform(self):
        self.create_post('Enter post text: ')

    @run_command
    def create_post(self, text):
        NewPost(text)
        db_record = DataBase()
        db_record.record_info(self.label())
        

class CommandUserPosts:
    def label(self):
        return 'User posts'
    
    def perform(self):
        while True:
            try:
                username = str(input('Enter username: '))
                twitter_acc = UserPosts(username)
                all_messages = twitter_acc.get_posts()
            except KeyboardInterrupt:
                return ('Cancel')
            else:
                self.posts_paginator(all_messages)
                break

    def posts_paginator(self, posts_array):
        for post in posts_array:
            print(f'============ {post["id"]} ============')
            print('{date}\n{text}'.format(date=post['date'], text=post['text']))


class History:
    def label(self):
        return 'User posts'

    # def perform(self):
    #     for read in self.read_db():
    #         print(self.read_db()[read])