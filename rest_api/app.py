from flask import Flask, jsonify, Response
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/ads'

mongo = PyMongo(app)

@app.route('/ads', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_ads():
    ads = mongo.db.test_collection.find()
    response = json_util.dumps(ads)
    return Response(response, mimetype='application/json') 

@app.route('/ads/<adId>', methods=['GET'])
@cross_origin(supports_credentials=True)
def get_ad(adId):
    ad = mongo.db.test_collection.find_one({'_id': ObjectId(adId)})
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json') 

@app.route('/ads/<adId>/like', methods=['POST'])
@cross_origin(supports_credentials=True)
def like_ad(adId):
    original_ad = mongo.db.test_collection.find_one({'_id': ObjectId(adId)})
    json_ad = json.loads(json_util.dumps(original_ad))
    new_likes = json_ad["likes"] + 1
    ad = mongo.db.test_collection.find_one_and_update(
            { '_id': ObjectId(adId) },
            { '$set':
                {
                    'likes': new_likes 
                }
            }
            )
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json') 

@app.route('/ads/<adId>/unlike', methods=['POST'])
@cross_origin(supports_credentials=True)
def unlike_ad(adId):
    original_ad = mongo.db.test_collection.find_one({'_id': ObjectId(adId)})
    json_ad = json.loads(json_util.dumps(original_ad))
    new_likes = json_ad["likes"] - 1
    ad = mongo.db.test_collection.find_one_and_update(
            { '_id': ObjectId(adId) },
            { '$set':
                {
                    'likes': new_likes
                }
            }
            )
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json')

@app.route('/ads/<adId>/dislike', methods=['POST'])
@cross_origin(supports_credentials=True)
def dislike_ad(adId):
    original_ad = mongo.db.test_collection.find_one({'_id': ObjectId(adId)})
    json_ad = json.loads(json_util.dumps(original_ad))
    new_dislikes = json_ad["dislikes"] + 1
    ad = mongo.db.test_collection.find_one_and_update(
            { '_id': ObjectId(adId) },
            { '$set':
                {
                    'dislikes': new_dislikes 
                }
            }
            )
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json') 

@app.route('/ads/<adId>/undislike', methods=['POST'])
@cross_origin(supports_credentials=True)
def undislike_ad(adId):
    original_ad = mongo.db.test_collection.find_one({'_id': ObjectId(adId)})
    json_ad = json.loads(json_util.dumps(original_ad))
    new_dislikes = json_ad["dislikes"] - 1
    ad = mongo.db.test_collection.find_one_and_update(
            { '_id': ObjectId(adId) },
            { '$set':
                {
                    'dislikes': new_dislikes
                }
            }
            )
    response = json_util.dumps(ad)
    return Response(response, mimetype='application/json')

@app.route('/ads/calculate_points', methods=['GET'])
@cross_origin(supports_credentials=True)
def calculate_points():
    collections = mongo.db.list_collection_names()
    print(collections)
    print(collections[0])
    collection_name = collections[0]
    docs = mongo.db.collection_name.find()
    json_ad = json.loads(json_util.dumps(docs))
    print(json_ad)
    ads = mongo.db.test_collection.find()
    response = json_util.dumps(ads)
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
