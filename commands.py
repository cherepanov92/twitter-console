# -*- coding: utf-8 -*-
from twitter_api import NewPost, UserPosts
from db_agent import DataBase
from viewer import UserPostsView, HistoryView

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

class CommandMainNewPost:

    def label(self):
        return 'New post'

    def perform(self):
        self.create_post('Enter post text: ')

    @command_runner
    def create_post(self, text):
        NewPost(text)


class CommandMainUserPosts:
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
        view = UserPostsView()
        view.perform(posts_array)


class CommandMainHistory:
    def label(self):
        return 'User posts'

    def perform(self):
        data = DataBase()
        self.viewer(data.get_history())

    def viewer(self, history_list):
        view = HistoryView()
        view.perform(history_list)

if __name__=='__main__':
    one = CommandUserPosts()
    one.perform()