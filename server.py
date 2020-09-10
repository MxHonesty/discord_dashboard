from sanic import Sanic
from sanic.response import json, text, html
from sanic.log import logger
from html_parser import get_final_html

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

@app.route('/servers')
async def servers(request):
    logger.info('SERVER LIST')
    page = get_final_html(bot.get_servers(), str(bot.client.user))
    return html(page)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 8000, debug = False)
