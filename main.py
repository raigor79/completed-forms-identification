import sys
from typing import Text

from loguru import logger
from aiohttp import web


async def post_handler(request):
    etext = await request.text()
    return web.Response(status=200, text=etext)


def main():
    pass


if __name__ == "__main__":
    logger.add(
        sys.stderr, 
        format="{time} {level} {message}", 
        filter="my_module", 
        level="INFO"
        )
    app = web.Application()
    
    app.add_routes([
        web.post('/get_form/', post_handler),               
    ])   
    try:
        web.run_app(app, host='localhost', port=8080)
    except KeyboardInterrupt:
        logger.info('Script the script was interrupted by clicking Ctrl+C')
    logger.info('Close')
