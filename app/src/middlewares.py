import json
from typing import Callable

from aiohttp import web
from aiohttp.web import middleware


@middleware
async def json_response(request: web.Request, handler: Callable) -> web.Response:
    try:
        resp = await handler(request)  # type: web.Response

        if hasattr(resp, 'text'):
            resp.text = json.dumps({
                'data': json.loads(resp.text)
            })

        return resp
    except web.HTTPClientError as e:
        e.text = json.dumps({
            'message': str(e),
        })
        e.content_type = "application/json"
        return e
