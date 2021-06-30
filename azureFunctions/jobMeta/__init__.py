import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import dbLocal2 as dbsetup

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    searchCollection="jobInfo_Meta"
    code = req.params.get('jnum')
    if not code:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('jnum')
    if code:
        try:
            url = dbsetup.monConnection
            client = pymongo.MongoClient(url)
            database = client[dbsetup.db]
            collection = database[searchCollection]

            result = collection.find({"jobNum":str(code)},{"_id":False})
            
            result = dumps(result)
            logging.info("Processing result")
            logging.info(len(result))
            m=list(result)
            logging.info(len(m))
        except:
            result="[{'Error':'No Result by that code. Enter numerical value. Example: code=12345'}]"
            logging.info("Error")
        if len(result)==2:
            result="[{'Error':'No Result by that code. Enter numerical value. Example: code=12345'}]"
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    else:
        try:
            url = dbsetup.monConnection
            client = pymongo.MongoClient(url)
            database = client[dbsetup.db]
            collection = database[searchCollection]

            result = collection.find({},{"_id":False})
            
            result = dumps(result)
            logging.info("Processing result")
            logging.info(len(result))
            m=list(result)
            logging.info(len(m))
        except:
            result="[{'Error':'No Result}]"
            logging.info("Error")
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
