# -*- coding: utf-8 -*-
from commands import NewPost, UserPosts, History

def get_routes():

    return{
        'New post':NewPost,
        'User posts':UserPosts,
        'History':History
    }

def perform_command(command):
    routes = get_routes()

    command_class = routes[command]
    command_inst = command_class()
    
    print(command_inst.perform())


def parse_user_input():
    input_function = input
    message = '{lb}Input your command: {commands} {lb}'\
        .format(commands=' | '.join(['New post', 'User posts', 'History']), lb='\n')

    return input_function(message)

def main():
    while True:
        command = parse_user_input()
        perform_command(command)

if __name__ == '__main__':
    main()