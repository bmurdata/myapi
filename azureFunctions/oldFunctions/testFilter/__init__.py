import logging
import re
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import dbLocal2 as dbsetup

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    searchCollection="jobInfo_Meta"
    allMatch="[A-Z]"
    code =  req.params.get('jnum')  if req.params.get('jnum') else "[0-9]"
    title= req.params.get('btitle')  if req.params.get('btitle') else allMatch
    cstitle= req.params.get('cstitle')  if req.params.get('cstitle') else allMatch
    longCat= req.params.get('hname')  if req.params.get('hname') else allMatch
    # logging.info("Arguements are: "+code+" for code and :"+title+" for title and "+longCat+" for hiring agency" )
 
    if code:
        logging.info("Found a code")
        try:
            url = dbsetup.monConnection
            client = pymongo.MongoClient(url)
            database = client[dbsetup.db]
            collection = database[searchCollection]
            myConditions=[
                {"HiringAgency":{"$regex":str(longCat),"$options":"-i"}},
                {"jobNum":{"$regex":str(code),"$options":"-i"}},
                {"Business Title":{"$regex":str(title),"$options":"-i"}},
                {"Civil Service Title":{"$regex":str(cstitle),"$options":"-i"}},
                ]
            #logging.info(myConditions)
            result = collection.find({'$and':myConditions},{"_id":False})
            # result = collection.find(myConditions[0],{"_id":False})
            # result = collection.find({"jobNum":{"$regex":str(code)}},{"_id":False})
            # result = collection.find({"jobNum":{"$regex":str(code)}},{"_id":False})
            # r1=collection.find({"jobNum":{"$regex":code+ "*"}},{"_id":False})
            result = dumps(result)
            #result=r1
            # logging.info("Processing result")
            # logging.info(len(result))

        except Exception as e:
            result="[{'Error':'No Result by "+str(code)+ "code. Enter numerical value. Example: code=12345'}]"
            logging.info("Error below:")
            logging.info(e)
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
