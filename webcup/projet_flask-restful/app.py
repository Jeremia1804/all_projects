from flask import Flask
from flask_restful import Api
from app.resources.UserController import UserResource

app = Flask(__name__)
api = Api(app)

api.add_resource(UserResource, '/users', '/users/<int:user_id>')