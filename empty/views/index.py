from aiohttp_jinja2 import template


@template('index.html')
async def healthcheck(request):
    request.app['logger'].info('INFO LOG')
    return {'title': 'WORKED'}
