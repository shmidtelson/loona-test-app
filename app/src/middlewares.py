import json
from typing import Callable

from aiohttp import web
from aiohttp.web import middleware


@middleware
async def json_handler(request: web.Request, handler: Callable) -> web.Response:
    request.json_fields = await request.json()
    resp = await handler(request)
    return resp
