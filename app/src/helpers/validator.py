from aiohttp import web
from cerberus import Validator


async def validate(data, schema) -> bool:
    v = Validator()

    if v.validate(data, schema) is False:
        raise web.HTTPBadRequest(reason='Data are not valid')

    return True
