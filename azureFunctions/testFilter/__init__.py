import logging
import re
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import dbLocal2 as dbsetup

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    searchCollection="jobMeta"

    code = req.params.get('jnum')+"*" if req.params.get('jnum') else "*"
    title=req.params.get('title')+"*" if req.params.get('title') else "*"
    shortCat=req.params.get('hiringCode')+"*" if req.params.get('hiringCode') else "*"
    longCat=req.params.get('hiringName')+"*" if req.params.get('hiringName') else "*"
    logging.info("Arguements are: "+code+" for code and :"+title+" for title and "+longCat+" for hiring agency" )
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
            myConditions=[
                #{"HiringAgency":{"$regex":str(longCat)}},
                {"jobNum":{"$regex":str(code)}},
                #{"Business Title":{"$regex":str(title)}},
                #{"Civil Service Title":{"$regex":str(title)}},
                {"_id":False}
                ]
            result = collection.find({"$and":myConditions})
            
            result = dumps(result)
            logging.info("Processing result")
            logging.info(len(result))
            m=list(result)
            logging.info(len(m))
        except:
            result="[{'Error':'No Result by "+str(code)+ "code. Enter numerical value. Example: code=12345'}]"
            logging.info("Error")
        if len(result)==2:
            result="[{'Error':'No Result by that code "+str(code)+". Enter numerical value. Example: code=12345'}]"
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
