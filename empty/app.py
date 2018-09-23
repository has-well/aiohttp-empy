from aiohttp import web
from .routes import setup_routes
from empty.middlewares import setup_middlewares
from logger import create_logger

import jinja2
import aiohttp_jinja2
import asyncpgsa


async def create_app(config: dict):
    app = web.Application()
    app['config'] = config
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.PackageLoader('empty', 'templates')
    )
    setup_routes(app)
    setup_middlewares(app)
    app['logger'] = create_logger(config)

    app.on_startup.append(on_start)
    app.on_cleanup.append(on_shutdown)
    return app


async def on_start(app):
    config = app['config']['db']
    app['pg'] = await asyncpgsa.create_pool(**config)


async def on_shutdown(app):
    await app['db'].close()
