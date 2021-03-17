from aiohttp import web

from src.dto.response import ErrorResponse, SuccessResponse
from src.repository.UserRepository import UserRepository
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
        params = await self.request.json()

        user_repository = UserRepository()

        user = user_repository.get_by_login(params.get('login'))
        if not user:
            return ErrorResponse('User not found')
        return web.json_response(user.check_password(params.get('password')))


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
        params = await self.request.json()

        try:
            creator = UserCreator()
            user = creator.create(
                params.get('login'),
                params.get('password')
            )
        except Exception as e:
            Logger.instance().info(e, exc_info=True)
            return ErrorResponse('Something went wrong')

        return SuccessResponse(user)
