import dbLocal2
db=dbLocal2.db
monConnection=dbLocal2.monConnection
from bson import json_util
import json
import pymongo

metaJobs="jobInfo_Meta"
client = pymongo.MongoClient(monConnection)
database=client[db]
def showItems(myCollection:str()):
    collec=database[myCollection]
    for item in collec.find():
        print(type(item))
        print(item)
metaCollection="jobInfo_Meta"
contentCollection="jobInfo_Content"
# showItems(metaCollection)

# json.dumps(result,default=json_util.default)
from flask import Flask
app = Flask(__name__)
def showOne(myCollection:str()):
    collec=database[myCollection]
    for item,val in enumerate(collec.find()):
        mydict=item
        print(val)
    
    #mydict=collec.find_one()

    return json.dumps(mydict)
@app.route('/')
def hello_world():
    return showOne(contentCollection)
