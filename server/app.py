from flask import Flask, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound
from models import db, User, Blogpost, User_blogposts

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

class Welcome(Resource):
    def get(self):
        response_message = {
            "message": "WELCOME TO THE BLOOMBLAS BLOGGING SITE API."
        }
        return make_response(response_message, 200)

api.add_resource(Welcome, '/')

class Users(Resource):
    def get(self):
        users = User.query.all()
        user_list = []
        for user in users:
            user_dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
            user_list.append(user_dict)
        return make_response(jsonify(user_list), 200)

api.add_resource(Users, '/users')

class UserByID(Resource):
    def get(self, id):
        user = User.query.get(id)
        if user:
            user_dict = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "blogposts": [
                    {
                        "id": user_blogpost.blogpost.id,
                        "name": user_blogpost.blogpost.name,
                        "description": user_blogpost.blogpost.description,
                    }
                    for user_blogpost in user.blogposts
                ]
            }
            return make_response(jsonify(user_dict), 200)
        else:
            return make_response(jsonify({"error": "User not found"}), 404)

api.add_resource(UserByID, '/users/<int:id>')

class Blogposts(Resource):
    def get(self):
        blogposts = Blogpost.query.all()
        blogpost_list = []
        for blogpost in blogposts:
            blogpost_dict = {
                "id": blogpost.id,
                "name": blogpost.name,
                "description": blogpost.description,
                "ratings": blogpost.ratings  # Corrected 'ratings' to 'rating'
            }
            blogpost_list.append(blogpost_dict)
        return make_response(jsonify(blogpost_list), 200)

api.add_resource(Blogposts, '/blogposts')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
