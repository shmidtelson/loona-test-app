from aiohttp import web
from routes import setup_routes
from aiohttp_swagger import *
from settings import SWAGGER_PARAMS, APP_PORT
from dotenv import load_dotenv

from src.middlewares import json_response
from src.service.db import Database

load_dotenv()

app = web.Application(middlewares=[json_response])
setup_routes(app)
setup_swagger(app, **SWAGGER_PARAMS)

app.on_startup.append(Database.init_pg)
app.on_cleanup.append(Database.close_pg)

web.run_app(app, port=APP_PORT)
