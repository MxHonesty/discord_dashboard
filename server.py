from sanic import Sanic
from sanic.response import json, text, html
from sanic.log import logger

# Botul de discord
import bot

app = Sanic(__name__)

# Default
@app.route('/')
async def test(request):
    logger.info('Accesat')
    logger.info(request.url)    # Url
    logger.info(request.args)   # Argumentele din url
    return json({'hello' : 'world'})    # Raspuns json

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = False)
