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

    def perform(self, data_list):
        self.print_posts(data_list)
        self.select_choice()

    def print_posts(self, data_list):
        for post in data_list:
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

class HistoryView:
    function = input
    # commands = ['Preview', 'Home', 'Cleaner', 'Next']
    commands = ['Home', 'Cleaner']
    message = '{br}Input your command: {commands} {br}' \
                .format(commands=' | '.join(commands), br='\n')

    def perform(self, data_list):
        self.print_records(data_list)
        self.select_choice()

    def print_records(self, records):
        for record in records:
            print('{decor} {date} {decor}'.format(decor='=============', date=record[2]))
            print(record[1])

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