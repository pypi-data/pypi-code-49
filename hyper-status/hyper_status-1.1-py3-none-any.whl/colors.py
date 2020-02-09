'''
> hyper_status
> Copyright (c) 2020 Xithrius
> MIT license, Refer to LICENSE for more info
'''


colors = {
    'gold': '\033[93m',
    'red': '\033[91m',
    'purple': '\033[95m',
    'green': '\033[92m',
    'blue': '\033[96m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'end': '\033[0m'
}


if __name__ == "__main__":
    print('\n'.join(f'{colors[y]}{y}{colors["end"]}' for y in colors if y != 'end'))
