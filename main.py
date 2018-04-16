# -*- coding: utf-8 -*-

def parse_user_input():
    input_function = input
    message = 'Input your command: {commands} \n'\
        .format(commands=' | '.join(['New post', 'User posts', 'History']))

    return input_function(message)

def main():
    while True:
        command = parse_user_input()

if __name__ == '__main__':
    main()