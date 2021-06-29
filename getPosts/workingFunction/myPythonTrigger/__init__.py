import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import dbsetup2 as dbsetup

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Get Collection trigger function processed a request.')

    try:
        url = dbsetup.myurl
        client = pymongo.MongoClient(url)
        database = client[dbsetup.db]
        collection = database['jobsByCode']

        result = collection.find({},{"_id":False})
        
        result = dumps(result)
        logging.info("Processing result")
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except Exception as e:
        print(e)
        return func.HttpResponse("Bad request.", status_code=400)
