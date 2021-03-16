from aiohttp import web


class SuccessResponse:
    data: dict = {}

    def __init__(self, data: dict):
        self.data = data

    def __repr__(self):
        return web.json_response(self)


class ErrorResponse:
    data: dict = {}
    message: str = ''

    def __init__(self, message: str, data: dict):
        self.data = data
        self.message = message

    def __repr__(self):
        return web.json_response(self)
