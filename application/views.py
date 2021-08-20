import aiohttp_jinja2
from aiohttp import web
from application.utils import check_link, shorten_url


class SiteHandler:

    def __init__(self, redis):
        self._redis = redis

    @aiohttp_jinja2.template('index.html')
    async def index_handler(self, request):
        if request.method == 'POST':
            form = await request.post()
            long_url = form['url']
            check_link(long_url)
            if await self._redis.get(long_url):
                pass
            else:
                await self._redis.incr("shortify:count")
                short_url = shorten_url()
                await self._redis.set(long_url, short_url)
            return web.json_response({"url": True})
        return {}
