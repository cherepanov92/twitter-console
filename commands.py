# -*- coding: utf-8 -*-
from twitter_api import NewPost, UserPosts
from db_agent import DataBase
# from viewer import *

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
    posts_list = []

    def label(self):
        return 'User posts'

    def perform(self):
        self.get_user_posts('Enter username: ')
        return self.posts_list

    @command_runner
    def get_user_posts(self, username):
        account = UserPosts(username)
        posts = account.get_posts()
        self.posts_list = posts


class CommandHistory:
    data = DataBase()

    def label(self):
        return 'History'

    def perform(self):
        return(self.data.get_history())

    def cleaner(self):
        self.data.cleaner()

if __name__=='__main__':
    one = CommandUserPosts()
    one.perform()