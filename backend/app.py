import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_pymongo import PyMongo

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Mongodb connection initialization to database gameStore'
app.config['MONGO_URI'] = "mongodb://datinguser:datinguserpasswd@mongodb_tinder:27017/tinderClone?authSource=admin"
mongo = PyMongo(app)

# Enable CORS (CORS is a library that enables cross-origin requests)
# For example different protocol, IP address, domain name or port
CORS(app)


# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong!")


# Routing
@app.route('/login', methods=['PUT'])
@cross_origin()
def login():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    user = mongo.db.users.find_one({"email": post_data['email']})
    if user is not None:
        if post_data['password'] == user['password']:
            response_object['message'] = 'Logged in successfully!'
            response_object['user'] = user

        else:
            response_object['message'] = 'Wrong password! Try again...'

    else:
        response_object['message'] = 'Email is wrong'

    return jsonify(response_object)


@app.route('/register', methods=['POST'])
@cross_origin()
def register():
    response_object = {'status': 'success'}
    post_data = request.get_json()

    email = post_data.get('email')
    if mongo.db.users.find_one({'email': email}) is None:
        mongo.db.users.insert({
            '_id': uuid.uuid4().hex,
            'email': email,
            'username': post_data.get('username'),
            'name': post_data.get('name'),
            'surname': post_data.get('surname'),
            'password': post_data.get('password'),
            'birthday': post_data.get('birthday'),
            'type': 'free'
        })

        response_object['message'] = 'User made!'

    else:
        response_object['message'] = 'Email already exists'

    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
