# -*- coding: utf-8 -*-
from commands import CommandNewPost, CommandUserPosts, CommandHistory
from viewer import MainView

def get_routes():

    return{
        'New post':CommandNewPost,
        'User posts':CommandUserPosts,
        'History':CommandHistory
    }

def perform_command(command):
    routes = get_routes()

    command_class = routes[command]
    command_inst = command_class()
    
    command_inst.perform()

def main():
    while True:
        command = MainView()
        perform_command(command.select_choice())

if __name__ == '__main__':
    main()