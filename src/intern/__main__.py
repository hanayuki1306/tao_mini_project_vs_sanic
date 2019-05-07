# from sanic import Sanic
# from sanic.views import HTTPMethodView
# from sanic.response import text

# app = Sanic('son_name')


from .somethingnews.xinchao import xinchao
from .somethingnews.tambiet import tambiet
from .somethingnews.class1 import bantengi
from .somethingnews.class0 import SimpleView
from .core import app


app.add_route(SimpleView.as_view(), '/')
app.add_route(bantengi.as_view(), '/bantengi')
app.add_route(xinchao.as_view(), '/xinchao')
app.add_route(tambiet.as_view(), '/tambiet')

app.run(host='0.0.0.0',port=8000)