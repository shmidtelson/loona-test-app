from aiohttp import web
from routes import setup_routes
from aiohttp_swagger import *
from settings import SWAGGER_PATH, APP_PORT, SWAGGER_UI_VERSION

app = web.Application()
setup_routes(app)
setup_swagger(app, swagger_url=SWAGGER_PATH, ui_version=SWAGGER_UI_VERSION)

web.run_app(app, port=APP_PORT)
