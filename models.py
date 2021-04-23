from flask_restful_swagger_3 import Resource, Api, Schema, swagger


class ArticleStats(Schema):
    type = "object"
    properties = {"visits": {"type": "integer"}}


class UserModel(Schema):
    type = "object"
    properties = {
        "id": {
            "type": "string",
        },
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