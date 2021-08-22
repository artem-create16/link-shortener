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
            response = await self._redis.get(long_url)
            if response:
                return web.json_response({"url": response.decode()})
            else:
                await self._redis.incr("shortify:count")
                short_url = shorten_url()
                await self._redis.set(short_url, long_url)
                short_url = "https://{host}:{port}/{path}".format(
                    host='localhost',
                    port=8080,
                    path=short_url)
                return web.json_response({"url": short_url})
        return {}

    async def redirect(self, request):
        short_id = request.match_info['uniq_ending']
        location = await self._redis.get(short_id)
        if not location:
            raise web.HTTPNotFound()
        return web.HTTPFound(location=location.decode())
