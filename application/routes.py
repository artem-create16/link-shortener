# from application.views import index_handler


def setup_routes(app, handler):

    app.router.add_get('/', handler.index_handler)
    app.router.add_post('/', handler.index_handler)
