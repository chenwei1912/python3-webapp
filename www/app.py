#!/usr/bin/env python3
#encoding=utf-8


import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)

    # 添加get响应方法
    app.router.add_route('GET', '/', index)

    # 用异步协程方法创建一个网络服务
    srv = yield from loop.create_server(app.make_handler(), '0.0.0.0', 9000)

    logging.info('server started at http://0.0.0.0:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()



if __name__ == '__main__':
    print('app.py execute')
