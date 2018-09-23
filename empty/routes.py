from .views import index

routes = {
    ('GET', '/', index.healthcheck, 'view')
}


def setup_routes(app):
    for route in routes:
        if len(route) > 4:
            app.router.add_route(route[0], route[1], route[2], name=route[3], expect_handler=route[4])
        else:
            app.router.add_route(route[0], route[1], route[2], name=route[3])


def setup_static(app):
    app.router.add_static('/static/', path='static', name='static', follow_symlinks=True)
