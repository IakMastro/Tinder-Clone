import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS
import pymongo

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)
mongo_client = pymongo.MongoClient("mongodb://datinguser:datinguserpasswd@ff4c716a611f:27017/")
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    query = mongo_client['test']['ping'].find_one()['text']
    return jsonify(query)


if __name__ == '__main__':
    app.run()
