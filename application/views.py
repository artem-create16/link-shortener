import aiohttp_jinja2
from aiohttp import web
from application.utils import check_link


routes = web.RouteTableDef()
CHARS = "abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
def encode(num, alphabet=CHARS):
    if num == 0:
        return alphabet[0]
    arr = []
    base = len(alphabet)
    while num:
        num, rem = divmod(num, base)
        arr.append(alphabet[rem])
    arr.reverse()
    return ''.join(arr)

class SiteHandler:

    def __init__(self, redis):
        self._redis = redis

    @aiohttp_jinja2.template('index.html')
    async def index_handler(self, request):
        if request.method == 'POST':
            form = await request.post()
            long_url = form['url']
            check_link(long_url)
            index = await self._redis.incr("shortify:count")
            path = encode(index)
            key = "shortify:{}".format(path)
            await self._redis.set(key, long_url)
            url = "http://{host}:{port}/{path}".format(
                host='localhost',
                port=1234,
                path=path)

            return web.json_response({"url": url})
        return {}
