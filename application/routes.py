def setup_routes(app, handler):
    app.router.add_get('/', handler.index_handler)
    app.router.add_post('/', handler.index_handler)
    app.router.add_get('/{uniq_ending}', handler.redirect)
    app.router.add_post('/{uniq_ending}', handler.redirect)
