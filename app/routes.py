from settings import API_PREFIX
from views import UserView, UserAuthView, UserRegisterView

routes = [
    ['user', UserView, 'user'],
    ['user/auth', UserAuthView, 'user.auth'],
    ['user/register', UserRegisterView, 'user.register'],
]


def setup_routes(app):
    for route in routes:
        app.router.add_view(API_PREFIX + route[0], route[1], name=route[2])
