import json
from typing import Callable

from aiohttp import web
from aiohttp.web import middleware


@middleware
async def json_response(request: web.Request, handler: Callable) -> web.Response:
    # resp
    resp = await handler(request)  # type: web.Response

    if hasattr(resp, 'text'):
        resp.text = json.dumps({
            'data': json.loads(resp.text)
        })

    return resp
