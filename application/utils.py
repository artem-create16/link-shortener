import aioredis
from aiohttp import web
import validators
import datetime


def check_link(link):
    if not validators.url(link):
        raise web.HTTPBadRequest(body='URL is not valid')
    return link


def shorten_url():
    time_now = datetime.datetime.now()
    uniq_ending = time_now.strftime('%y%-m%H%M%S%f')
    return uniq_ending
