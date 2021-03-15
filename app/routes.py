from settings import API_PREFIX
from views import UserView, UserAuthView, UserRegisterView

routes = [
    ['user', UserView],
    ['user/auth', UserAuthView],
    ['user/register', UserRegisterView],
]


def setup_routes(app):
    for route in routes:
        app.router.add_view(API_PREFIX + route[0], route[1], name=route[0].replace('/', '.'))
