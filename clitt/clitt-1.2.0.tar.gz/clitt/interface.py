import os
from datetime import datetime
from colorama import init, Fore, Style
init(autoreset=True)

def split_string(string, chunk_size):
    chunks = len(string)
    return [ string[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

def show_tweet(tweet, reverse=False):
    rows, columns = os.popen('stty size', 'r').read().split()
    separator = '-'
    blank = ' '
    header = f'{tweet.user.name} - {Fore.CYAN}@{tweet.user.screen_name}{Style.RESET_ALL}'
    text = tweet.text
    line_size = int(columns)
    text = split_string(text, line_size - 4)
    print(f'+{separator * (line_size - 2)}+')
    print(f'| {header}{ blank * (line_size - len(header) + 6)}|')
    for line in text:
        print(f'| {line}{blank * (line_size - len(line) - 3)}|')
    print('+' + '-' * (line_size - 2) + '+')

def show_message(message, sender, reverse=False):
    rows, columns = os.popen('stty size', 'r').read().split()
    separator = '-'
    blank = ' '
    date = datetime.fromtimestamp(int(message.created_timestamp[0:10]))
    header = f'{sender.name} - {Fore.CYAN}@{sender.screen_name}{Style.RESET_ALL} - {date}'
    line_size = int(columns)
    text = split_string(message.message_create["message_data"]["text"], line_size - 4)
    
    print(f'+{separator * (line_size - 2)}+')
    if reverse:
        print(f'|{ blank * (line_size - len(header) + 6)}{header} |')
        for line in text:
            print(f'|{blank * (line_size - len(line) - 3)}{line} |')
    else:
        print(f'| {header}{ blank * (line_size - len(header) + 6)}|')
        for line in text:
            print(f'| {line}{blank * (line_size - len(line) - 3)}|')  
    print('+' + '-' * (line_size - 2) + '+')

def show_user(user):
    rows, columns = os.popen('stty size', 'r').read().split()
    line_size = int(columns)
    separator = '-'
    blank = ' '
    header = f'{user.name} - {Fore.CYAN}@{user.screen_name}{Style.RESET_ALL}'
    bio = f'Bio: {user.description}'
    bio = split_string(bio, line_size - 4)
    followers = f'Followers: {user.followers_count}'
    
    print(f'+{separator * (line_size - 2)}+')
    print(f'| {header}{ blank * (line_size - len(header) + 6)}|')
    for line in bio:
        print(f'| {line}{ blank * (line_size - len(line) - 3)}|')
    print(f'| {followers}{ blank * (line_size - len(followers) - 3)}|')
    print('+' + '-' * (line_size - 2) + '+')