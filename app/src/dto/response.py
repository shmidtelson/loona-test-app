import json

from aiohttp import web


class SuccessResponse:
    data: dict = {}

    def __init__(self, data: dict):
        self.data = data

    def default(self):
        return web.json_response(self)


class ErrorResponse:
    data: dict = {}
    message: str = ''

    def __init__(self, message: str, data=None):
        if data is None:
            data = {}
        self.data = data
        self.message = message

    def default(self):
        return web.json_response(self)
