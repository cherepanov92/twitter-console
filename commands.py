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
                twitter_acc = UserPosts(username)
                all_messages = twitter_acc.get_posts()
            except KeyboardInterrupt:
                return ('Cancel')
            else:
                self.posts_paginator(all_messages)
                break

    def posts_paginator(self, posts_array):
        '''
        paginator_page = 1
        col_messages_in_page = 20
        start = int(paginator_page * col_messages_in_page)
        finish = int(start + col_messages_in_page)
        '''
        for post in posts_array:
            print(f'============ {post["id"]} ============')
            print('{date}\n{text}'.format(date=post['date'], text=post['text']))

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