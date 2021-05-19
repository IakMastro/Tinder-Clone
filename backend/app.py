import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_pymongo import PyMongo

# Configuration
DEBUG = True

# Initialize app
app = Flask(__name__)
app.config.from_object(__name__)

# Mongodb connection initialization to database gameStore'
app.config['MONGO_URI'] = "mongodb://datinguser:datinguserpasswd@mongodb:27017/tinderClone?authSource=admin"
mongo = PyMongo(app)

# Enable CORS (CORS is a library that enables cross-origin requests)
# For example different protocol, IP address, domain name or port
CORS(app, resources={r'/*': {'origins': '*'}})


# Sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify("pong!")


# Routing
# TODO: REST API functions here

if __name__ == '__main__':
    app.run()
