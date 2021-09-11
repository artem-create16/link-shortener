from aiohttp import web
import validators
from hashids import Hashids


def check_link(link):
    if not validators.url(link):
        raise web.HTTPBadRequest(body='URL is not valid')
    return link


def shorten_url(num):
    hashids = Hashids(salt="Here is my salt150173095")
    uniq = hashids.encode(num)
    return uniq
