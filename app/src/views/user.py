import jwt
from aiohttp import web

from settings import JWT_SECRET
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
           "404":
               description: User not found
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

        user_repository = UserRepository(self.request.app['db'])
        user = await user_repository.get_by_login(params.get('login'))
        if not user:
            raise web.HTTPNotFound(reason='User not found')

        user = user[0]

        if not user.check_password(params.get('password')):
            raise web.HTTPBadRequest(reason='Wrong password')

        delattr(user, 'password')
        encoded = jwt.encode({'user': {
            'id': str(user.id),
            'login': user.login,
        }}, JWT_SECRET, algorithm='HS256')

        return web.json_response({
            "token": encoded,
        })


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


class UserMeView(web.View):
    async def get(self) -> web.Response:
        """
        ---
        description: User me (information.
        tags:
        - User
        produces:
        - application/json
        responses:
            "200":
               description: User info
            "404":
               description: User not found
        """
        # params = await self.request.json()
        # schema = {'token': {'required': True, "type": 'string'}}
        # await validate(params, schema)

        # schema = {
        #     "login": {
        #         "required": True,
        #         "type": "string"
        #     },
        #     "password": {
        #         "required": True,
        #         "type": "string"
        #     },
        # }
        # await validate(params, schema)
        #
        # creator = UserCreator(self.request.app['db'])
        # user = await creator.create(
        #     params.get('login'),
        #     params.get('password')
        # )
        if not self.request.get('payload'):
            raise web.HTTPBadRequest(reason='Wrong request')

        user_payload = self.request['payload']['user']

        repository = UserRepository(self.request.app['db'])
        user = await repository.get_by_id(user_payload['id'])

        if not user:
            raise web.HTTPNotFound(reason='User not found')

        return web.json_response(UserModelSerializer(user[0]).serialize())

