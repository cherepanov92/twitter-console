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