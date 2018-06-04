#!/usr/bin/env python3
#encoding=utf-8

__author__ = 'Ethan Chen'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }


if __name__ == '__main__':
    print('handlers.py execute')
