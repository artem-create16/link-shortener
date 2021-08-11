from aiohttp import web
from application import init_func

app = init_func()

if __name__ == '__main__':
    web.run_app(app)
