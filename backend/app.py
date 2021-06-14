import datetime
import uuid

from flask import Flask, jsonify, request, redirect, url_for
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
CORS(app, resources={r'/*': {'origins': '*'}})


# Routing
@app.route('/login', methods=['PUT'])
@cross_origin()
def login():
    response_object = {}
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
    response_object = {}
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
            'gender': post_data.get('gender'),
            'weight': int(post_data.get('weight')),
            'height': int(post_data.get('height')),
            'hair_colour': post_data.get('hair_colour'),
            'eye_colour': post_data.get('eye_colour'),
            'bio': post_data.get('bio'),
            'pfp': 'default.jpg',
            'type': 'free'
        })

        response_object['message'] = 'User made!'
    else:
        response_object['message'] = 'Email already exists'

    return jsonify(response_object)


@app.route('/user/<user_id>', methods=['PUT', 'GET'])
@cross_origin()
def single_user(user_id):
    response_object = {}

    if request.method == 'GET':
        response_object['user'] = mongo.db.users.find_one({"_id": user_id})

    elif request.method == 'PUT':
        post_data = request.get_json()

        mongo.db.users.update_one({"_id": user_id}, {
            "$set": {
                'name': post_data.get('name'),
                'surname': post_data.get('surname'),
                'email': post_data.get('email'),
                'birthday': post_data.get('birthday'),
                'gender': post_data.get('gender'),
                'weight': int(post_data.get('weight')),
                'height': int(post_data.get('height')),
                'hair_colour': post_data.get('hair_colour'),
                'eye_colour': post_data.get('eye_colour'),
                'bio': post_data.get('bio')
            }
        })

        response_object['message'] = "Your info has been updated!"

    return jsonify(response_object)


@app.route('/referral/<code>')
@cross_origin()
def check_code(code):
    response_object = {}

    if mongo.db.users.find_one({"username": code}) is not None:
        response_object['message'] = 'OK'

    else:
        response_object['message'] = 'NOT FOUND'

    return jsonify(response_object)


def get_users(users):
    query = []

    for user in users:
        del user['password']
        query.append(user)

    return query


@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def all_users():
    response_object = {}

    if request.method == 'GET':
        response_object['users'] = get_users(mongo.db.users.find())
    elif request.method == 'POST':
        post_data = request.get_json()
        search_filter = post_data.get('filter')
        response_object['users'] = get_users(mongo.db.users.find(search_filter))

    return jsonify(response_object)


@app.route("/img/<path:filename>", methods=["GET"])
@cross_origin()
def get_img(filename):
    return mongo.send_file(filename)


@app.route("/img/<path:filename>", methods=["POST"])
@cross_origin()
def save_image(filename):
    if 'photo' in request.files:
        photo = request.files['photo']
        mongo.save_file(filename, photo)
        mongo.db.users.update_one({'username': request.form.get('user')}, {
            '$set':
                {
                    'pfp': filename,
                }
        })


@app.route("/prime/<user_id>", methods=["PUT"])
@cross_origin()
def prime_user(user_id):
    mongo.db.users.update_one({"_id": user_id}, {
        '$set': {
            'type': 'premium'
        }
    })


if __name__ == '__main__':
    app.run()
