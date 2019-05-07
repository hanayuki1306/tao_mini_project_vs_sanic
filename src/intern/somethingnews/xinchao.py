
from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text


class xinchao(HTTPMethodView):
    def get(self, request):
        return text('xin chao')

# app.add_route(xinchao.as_view(), '/xinchao')
