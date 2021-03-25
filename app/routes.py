from settings import API_PREFIX
from src.views import UserView, UserAuthView, UserRegisterView, UserMeView

routes = [
    ['user', UserView, 'user'],
    ['user/me', UserMeView, 'user.me'],
    ['user/auth', UserAuthView, 'user.auth'],
    ['user/register', UserRegisterView, 'user.register'],
]


def setup_routes(app):
    for route in routes:
        app.router.add_view(API_PREFIX + route[0], route[1], name=route[2])
