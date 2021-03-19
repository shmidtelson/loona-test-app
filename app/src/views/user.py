from aiohttp import web

from src.helpers.validator import validate
from src.repository.UserRepository import UserRepository
from src.serializers.UserModelSerializer import UserModelSerializer
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
            return web.json_response('User not found', status=404)
        return web.json_response(user.check_password(params.get('password')))


class UserRegisterView(web.View):
    async def post(self) -> web.Response:
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

        schema = {
            "login": {
                "required": True,
                "type": "string"
            },
            "password": {
                "required": True,
                "type": "string"
            },
        }
        await validate(params, schema)

        creator = UserCreator(self.request.app['db'])
        user = await creator.create(
            params.get('login'),
            params.get('password')
        )

        return web.json_response(UserModelSerializer(user).serialize())
