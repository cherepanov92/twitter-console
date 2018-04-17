# -*- coding: utf-8 -*-

class MainView:
    function = input
    commands = ['New post', 'User posts', 'History']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def select_choice(self):
        while True:
            try:
                choice = self.function(self.message)
                if choice not in self.commands:
                    raise Exception('Enter correct command!')
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print('exit')
                break
            else:
                return choice

class UserPostsView:
    function = input
    commands = ['Preview', 'Home', 'Next']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def perform(self, post_list):
        self.print_posts(post_list)
        self.select_choice()

    def print_posts(self, posts_list):
        for post in posts_list:
            print('{decor} {post_id} {decor}'.format(decor='=============================', post_id=post['id']))
            print('{}\n{}'.format(post['date'], post['text']))

    def select_choice(self):
        while True:
            try:
                choice = self.function(self.message)
                if choice not in self.commands:
                    raise Exception('Enter correct command!')
            except Exception as e:
                print(e)
            except KeyboardInterrupt:
                print('exit')
                break
            else:
                return choice

if __name__=='__main__':
    one = UserPostsView()
    print(one.select_choice())