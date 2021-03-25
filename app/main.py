from aiohttp import web
from aiohttp_jwt import JWTMiddleware

from routes import setup_routes
from aiohttp_swagger import *
from settings import SWAGGER_PARAMS, APP_PORT, JWT_SECRET, JWT_ALGORITHMS
from dotenv import load_dotenv

from src.middlewares import json_response
from src.service.db import Database

load_dotenv()

app = web.Application(middlewares=[
    JWTMiddleware(
        JWT_SECRET,
        algorithms=JWT_ALGORITHMS,
        credentials_required=False,
        request_property='payload',
    ),
    json_response,
],
    debug=True
)
setup_routes(app)
setup_swagger(app, **SWAGGER_PARAMS)

app.on_startup.append(Database.init_pg)
app.on_cleanup.append(Database.close_pg)

web.run_app(app, port=APP_PORT)
