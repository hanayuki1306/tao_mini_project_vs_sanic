from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text

class tambiet(HTTPMethodView):
    def get(self, request):
        return text('tambiet')

# app.add_route(tambiet.as_view(), '/tambiet')