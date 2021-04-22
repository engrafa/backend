from flask import Flask, request
from flask_restful import reqparse
from flask_cors import CORS
from flask_restful_swagger_3 import Resource, Api, Schema, swagger


class ArticleStats(Schema):
    type = "object"
    properties = {"visits": {"type": "integer"}}


class UserModel(Schema):
    type = "object"
    properties = {
        "id": {"type": "string",},
        "name": {"type": "string"},
        "user_type": {
            "type": "string",
            "enum": ["admin", "member", "regular"],
            "nullable": True,
        },
    }
    required = ["name"]


class ArticleModel(Schema):
    type = "object"
    properties = {
        "id": {"type": "string"},
        "name": {"type": "string"},
        "content": {"type": "string"},
        "stats": ArticleStats,
        "author": UserModel,
    }
    required = ["content"]


class Articles(Resource):
    @swagger.tags(["article"])
    @swagger.response(
        response_code=200, description="Article list retrieved successfully"
    )
    def get(self):
        # ArticleModel(**data)
        return "Not implemented", 500

    @swagger.tags(["article"])
    @swagger.response(response_code=201, description="Article created successfully")
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("content", type=str, default="")
        args = parser.parse_args()
        return "Not implemented", 500


class Article(Resource):
    @swagger.tags(["article"])
    @swagger.response(response_code=200, description="Article retrieved successfully")
    @swagger.response(
        response_code=404, description="Article does not exist or is inaccessible"
    )
    def get(self, _id):
        # ArticleModel(**data)
        return "Not implemented", 500


app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Articles, "/articles")
api.add_resource(Article, "/articles/<string:_id>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
