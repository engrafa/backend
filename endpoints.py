from flask_restful import reqparse
from flask_restful_swagger_3 import Resource, swagger
from models import UserModel, ArticleStats, ArticleModel


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
