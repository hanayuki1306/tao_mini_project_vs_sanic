from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text


class bantengi(HTTPMethodView):
    def get(self, request):
        return text('XIn hay nhap ten cua ban')

# app.add_route(bantengi.as_view(), '/bantengi')