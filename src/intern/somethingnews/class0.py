from sanic import Sanic
from sanic.views import HTTPMethodView
from sanic.response import text



class SimpleView(HTTPMethodView):

  def get(self, request):
      return text('I am get method')

  def post(self, request):
      return text('I am post method')

  def put(self, request):
      return text('I am put method')

  def patch(self, request):
      return text('I am patch method')

  def delete(self, request):
      return text('I am delete method')


    # app.add_route(SimpleView.as_view(), '/')