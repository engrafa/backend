from flask import Flask
from flask_cors import CORS
from flask_restful_swagger_3 import Api
from endpoints import Articles, Article

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Articles, "/articles")
api.add_resource(Article, "/articles/<string:_id>")
