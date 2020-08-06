from flask import Flask, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ads'

mongo = PyMongo(app)

@app.route('/ads', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_ads():
    ads = mongo.db.testCollection.find()
    response = json_util.dumps(ads)
    return Response(response, mimetype='application/json') 

@app.route('/ads/<adId>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_ad(adId):
    ad = mongo.db.testCollection.find_one({'_id': ObjectId(adId)})
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json') 

@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
            'message': 'Ad not found: ' + request.url,
            'status': 404
            })
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True)
