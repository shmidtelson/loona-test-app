from aiohttp import web
from routes import setup_routes
from aiohttp_swagger import *
from settings import SWAGGER_PARAMS, APP_PORT

app = web.Application()
setup_routes(app)
setup_swagger(app, **SWAGGER_PARAMS)

web.run_app(app, port=APP_PORT)
