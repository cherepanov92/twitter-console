# -*- coding: utf-8 -*-
# from commands import CommandMainNewPost, CommandMainUserPosts, CommandMainHistory
from viewer import MainView

# def get_routes():
#
#     return{
#         'New post':CommandMainNewPost,
#         'User posts':CommandMainUserPosts,
#         'History':CommandMainHistory
#     }
#
# def perform_command(command):
#     routes = get_routes()
#
#     command_class = routes[command]
#     command_inst = command_class()
#
#     command_inst.perform()

def main():
    # while True:
    command = MainView()
    command.select_choice()

if __name__ == '__main__':
    main()