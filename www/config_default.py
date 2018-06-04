#!/usr/bin/env python3
#encoding=utf-8

'''
Default configurations.
'''

__author__ = 'Ethan Chen'

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '378540',
        'db': 'awesome'
    },
    'session': {
        'secret': 'Awesome'
    }
}


if __name__ == '__main__':
    print('config_default.py execute')
