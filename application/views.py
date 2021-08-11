from aiohttp import web


async def index_handler(request):
    return web.Response(text='Hello Aiohttp!')
