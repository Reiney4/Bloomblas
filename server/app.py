from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import NotFound


from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


from flask_bcrypt import Bcrypt  # Import Flask-Bcrypt for password hashing


from flask_cors import CORS
from models import db, User, Blogpost, User_blogposts

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'your_secret_key'


migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)


jwt = JWTManager(app)

bcrypt = Bcrypt(app)


# Replace this with your actual User model
class UserData:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        print(request.get_json())
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')

        # Check if the required data is provided
        if not email or not username or not password:
            return make_response({'message': 'Missing required data'}, 400)

        # Check if the email is already registered
        if User.query.filter_by(email=email).first():
            return make_response({'message': 'Email is already registered'}, 400)

        # Hash the password before storing it
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Create a new user
        # new_user = UserData(email=email, username=username, password=hashed_password)
        final_new_user = User(**{"email": email, "username": username, "password": hashed_password})
        db.session.add(final_new_user)
        db.session.commit()

        # Identity can be any data that is json serializable
        access_token = create_access_token(identity=email)
        userdata = {'user_email': email, 'access_token': access_token}
        return make_response(userdata, 201)  # 201 Created status code

api.add_resource(UserRegister, '/users/register')



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
                "title": blogpost.title,
                "author": blogpost.author,
                "image_link": blogpost.image_link,  # Added "image_link
                "description": blogpost.description,
                "ratings": blogpost.ratings  # Corrected 'ratings' to 'rating'
            }
            blogpost_list.append(blogpost_dict)
        return make_response(jsonify(blogpost_list), 200)

api.add_resource(Blogposts, '/blogposts')




# Replace this with your actual user authentication logic
# def authenticate(email, password):
#     # Example: Check if email and password match in your database
#     user = User(email, password)
#     if user:  # Replace with your actual authentication logic
#         return user

# Example resource to handle user login
# class UserLogin(Resource):
#     def post(self):
#         data = request.get_json()
#         print(data)
#         email = data.get('email')
#         password = data.get('password')
#
#         user = authenticate(email, password)
#
#         if not user:
#             return {'message': 'Invalid credentials'}, 401
#
#         # Identity can be any data that is json serializable
#         access_token = create_access_token(identity=email)
#         return {'user_email': email, 'access_token': access_token}


def check_password(self, password):
    return bcrypt.check_password_hash(self.password, password)


class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # Check if the required data is provided
        if not email or not password:
            return make_response({'message': 'Missing required data'}, 400)

        user = User.query.filter_by(email=email).first()

        # Check if the user exists
        if not user:
            return make_response({'message': 'User not found'}, 401)

        print(user.password)

        # Check if the provided password is correct
        print(bcrypt.check_password_hash(user.password, password))

        if not bcrypt.check_password_hash(user.password, password):
            return make_response({'message': 'Invalid password'}, 401)

        # Generate access token for the user
        access_token = create_access_token(identity=email)
        userdata = {'user_email': email, 'access_token': access_token}
        return make_response(userdata, 200)

api.add_resource(UserLogin, '/users/login')


# Example protected resource
class ProtectedResource(Resource):
    @jwt_required()
    def get(self):
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return {'user_email': current_user}, 200

api.add_resource(ProtectedResource, '/protected')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)