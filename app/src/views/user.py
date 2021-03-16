from aiohttp import web

from src.dto.response import ErrorResponse, SuccessResponse
from src.service.abstract.LoggerAbstract import LoggerAbstract
from src.service.creator import UserCreator
from src.service.singleton.Logger import Logger


class UserView(web.View):
    async def get(self):
        """
        ---
        description: Get User.
        tags:
        - User
        produces:
        - text/plain
        responses:
           "200":
               description: successful operation. Return "pong" text
           "405":
               description: invalid HTTP Method
        """
        return web.json_response({"message": "good"})


class UserAuthView(web.View):
    async def post(self):
        """
        ---
        description: Post User.
        tags:
        - User
        produces:
        - application/json
        responses:
           "200":
               description: User registered successful
           "409":
               description: User already exists
        """
        return web.json_response({"message": "good"})


class UserRegisterView(web.View):
    async def post(self):
        """
        ---
        description: User register.
        tags:
        - User
        produces:
        - application/json
        responses:
            "200":
               description: User registered successful
            "409":
               description: User already exists
        """
        creator = UserCreator()
        try:
            user = creator.create(
                self.request.get('login'),
                self.request.get('password')
            )
        except Exception as e:
            Logger.instance().info(e, exc_info=True)
            return ErrorResponse('Something went wrong')

        return SuccessResponse(user)
