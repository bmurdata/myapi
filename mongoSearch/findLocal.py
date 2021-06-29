# Tired and will fix up later. More of a playground to learn Mongo, Flask Pymongo, and other stuff.
from weakref import ProxyTypes
import dbLocal2
db=dbLocal2.db
monConnection=dbLocal2.monConnection
from bson import json_util
import json
# import pymongo

from flask_pymongo import PyMongo
from flask import Flask, jsonify
from bson.json_util import dumps, loads
app = Flask(__name__)
# client = pymongo.MongoClient(monConnection)
app.config["MONGO_URI"]=monConnection

database=PyMongo(app)
def showItems(myCollection:str()):
    collec=database.db.jobsByCode.find()
    docs=[doc for doc in collec]
    return docs
    return loads(dumps(collec))

jobsByCode="jobsByCode"
metaCollection="jobInfo_Meta"
contentCollection="jobInfo_Content"

def showOne(myCollection:str()):
    collec=database.db.jobsByCode.find_one_or_404()
    print(collec)
    return collec
# print(showItems(contentCollection))
@app.route('/')
def index():
    jobs=database.db.jobsByCode.find({},{'_id': False})
    m={'cursor': [job for job in jobs]}
    # m= [job for job in jobs]
    return dumps(m)
@app.route('/jobs')
def jobs():
    return jsonify(showItems(jobsByCode))


if __name__=="__main__":
    app.run()