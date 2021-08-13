import aioredis
from aiohttp import web

# ShortifyRequest = t.Dict({t.Key('url'): t.URL})
#
# def fetch_url(data):
#     try:
#         data = ShortifyRequest(data)
#     except t.DataError:
#         raise web.HTTPBadRequest()
#     return data['url']
