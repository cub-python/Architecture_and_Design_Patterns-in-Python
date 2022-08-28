from pumba_framework.main import Framework
from urls import fronts
from wsgiref.simple_server import make_server

from views import routes

application = Framework(routes, fronts)

with make_server('', 8989, application) as httpd:
    print("Запуск на порту 8989...")
    httpd.serve_forever()
