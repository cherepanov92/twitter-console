# -*- coding: utf-8 -*-
from twitter_api import NewPost, UserPosts


class CommandNewPost:

    def perform(self):
        while True:
            try:
                text = str(input('Enter post text: '))
                TwitterNewPost(text)
            except KeyboardInterrupt:
                return('Cancel')
            else:
               return('post was published')
        

class CommandUserPosts:
    
    def perform(self):
        while True:
            try:
                username = str(input('Enter username: '))
                user_posts = UserPosts(username)
            except KeyboardInterrupt:
                return ('Cancel')
            else:
                return user_posts


class History:
    def read_db(self):
        db = {'1': 'NewPost',
              '2': 'UserPosts',
              '3': 'UserPosts',
              '4': 'NewPost',
              '5': 'NewPost',
              '6': 'UserPosts',
              '7': 'NewPost'}
        
        return db

    def perform(self):
        for read in self.read_db():
            print(self.read_db()[read])