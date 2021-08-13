import aiohttp_jinja2
from aiohttp import web

routes = web.RouteTableDef()


class SiteHandler:

    def __init__(self, redis):
        self._redis = redis

    @aiohttp_jinja2.template('index.html')
    async def index_handler(self, request):
        print('Im here', flush=True)
        if request.method == 'POST':
            form = await request.post()
            long_url = form['url']
            key = 1
            await self._redis.set(key, long_url)
        return {}
