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

    def label(self):
        return 'User posts'

    def perform(self, start_id = None):
        if not start_id:
            self.get_user_posts('Enter username: ')

        return self.get_posts(start_id)

    def get_posts(self, id):
        posts = self.account.get_posts(start_id = id)
        return posts

    @command_runner
    def get_user_posts(self, username):
        self.account = UserPosts(username)



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