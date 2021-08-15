import aioredis
from aiohttp import web
import validators


def check_link(link):
    if not validators.url(link):
        raise web.HTTPBadRequest(body='URL is not valid')
    return link
