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
    print(command_class.test_message)

def parse_user_input():
    input_function = input
    message = 'Input your command: {commands} \n'\
        .format(commands=' | '.join(['New post', 'User posts', 'History']))

    return input_function(message)

def main():
    while True:
        command = parse_user_input()
        perform_command(command)

if __name__ == '__main__':
    main()