# -*- coding: utf-8 -*-
from twitter_api import NewPost, UserPosts
from db_agent import DataBase

def command_runner(method):
    def command_pagination(self, text):
        while True:
            try:
                user_input = str(input(text))
            except KeyboardInterrupt:
                print('Cancel')
                break
            else:
                print('Success')
                db_record = DataBase()
                db_record.record_info(' '.join([self.label(), user_input]))
                return method(self, user_input)
    return command_pagination

class CommandNewPost:

    def label(self):
        return 'New post'

    def perform(self):
        self.create_post('Enter post text: ')

    @command_runner
    def create_post(self, text):
        NewPost(text)


class CommandUserPosts:
    def label(self):
        return 'User posts'
    
    def perform(self):
        self.get_user_posts('Enter username: ')

    @command_runner
    def get_user_posts(self, username):
        account = UserPosts(username)
        posts = account.get_posts()
        self.posts_paginator(posts)

    def posts_paginator(self, posts_array):
        print(posts_array)


class CommandHistory:
    def label(self):
        return 'User posts'

    def perform(self):
        # for read in self.read_db():
        print('History')
if __name__=='__main__':
    one = CommandUserPosts()
    one.perform()