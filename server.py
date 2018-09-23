import argparse
import asyncio
import logging
import aiohttp
from empty import create_app
from empty.settings import load_config

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    print("Library uvloop is not available")

parser = argparse.ArgumentParser(description="App")
parser.add_argument('--host', help="Host to listen", default="127.0.0.3")
parser.add_argument('--port', help="Port", default=9000)
parser.add_argument(
    '--dev',
    action="store_true",
    help="Autoreload")
parser.add_argument("-c", "--config", type=argparse.FileType('r'),
                    help="Config file"
                    )

args = parser.parse_args()
app = create_app(config=load_config(args.config))
access_log = None
if args.dev:
    print("Dev mod")
    import aioreloader

    aioreloader.start()
    access_log = logging.getLogger('aiohttp.access')

if __name__ == '__main__':
    aiohttp.web.run_app(app, host=args.host, port=args.port, access_log=access_log)
