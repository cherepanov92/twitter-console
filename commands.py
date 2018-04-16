# -*- coding: utf-8 -*-

class NewPost:

    def perform(self):
        print('new post')


class UserPosts:

    def search_message(self, username):
        user_db = {'test': ['message 1','message 2','message 3','message 4','message 5','message 6']}
        return user_db[username]
    
    def perform(self):
        for message in self.search_message('test'):
            print(message)


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