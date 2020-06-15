from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson import ObjectID
#from bson.objectid import ObjectId
import json 
app= Flask(__name__)
# connect your mongodb server after install
app.config["MONGO_URI"] = 'mongodb://localhost:27017/demo2'
mongo = PyMongo(app)
CORS(app)

db = mongo.db.demo2

@app.route('/',methods=["GET","POST"])
def getpost():
    if request.method == "GET":
        o = []
        for i in db.find():
            o.append({"_ID":str(ObjectID(i["_id"])),"name":i["name"],"email":i["email"],"password":i["password"]})
        return jsonify(o)

    elif request.method =="POST":
        db.insert({"name":request.json["name"], "email":request.json["email"],  "password":request.json["password"],})
        return jsonify(str(ObjectId(id)))
    
@app.route('/<id>', methods=["DELETE","PUT"])
def deleteput(id):
    if request.method == "DELETE":
        db.delete_one({"_id":ObjectId(id)})
        return jsonify({"message": "deleted"})

    elif request.method =="PUT":
        db.update({"_id":ObjectID(id)}, {"$set":{
            "name": request.json["name"],
            "email": request.json["email"],
            "password": request.json["password"]
        }})
        return jsonify({"message":"updated"})
@app.route('/getone/<id>', methods=["GET"])
def getone(id):
    res = db.find_one({"_id":ObjectId(id)})
    print(res)
    return {"_ID":str(ObjectId("_id")), "name":res["name"], "email":res["email"], "passwword":res["password"]}
