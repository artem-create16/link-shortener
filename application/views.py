import aiohttp_jinja2
from aiohttp import web

routes = web.RouteTableDef()


@aiohttp_jinja2.template('index.html')
async def index_handler(request):
    print('Im here', flush=True)
    if request.method == 'POST':
        form = await request.post()
        print('FORM URL IS -->', form['url'], flush=True)
    return {}
