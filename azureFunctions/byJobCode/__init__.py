import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import dbLocal2 as dbsetup

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python byJobCode trigger function processed a request.')
    searchCollection="jobsByCode"
    allMatch="[A-Z]"
    code =  req.params.get('jnum')  if req.params.get('jnum') else "[0-9]"
    title= req.params.get('btitle')  if req.params.get('btitle') else allMatch
    acode= req.params.get('acode')  if req.params.get('acode') else "[0-9]"
    longCat= req.params.get('hname')  if req.params.get('hname') else allMatch
 
    if code:
        logging.info("Found a code")
        try:
            url = dbsetup.monConnection
            client = pymongo.MongoClient(url)
            database = client[dbsetup.db]
            collection = database[searchCollection]
            myConditions=[
                {"longcategory":{"$regex":str(longCat),"$options":"-i"}},
                {"jobNum":{"$regex":str(code),"$options":"-i"}},
                {"title":{"$regex":str(title),"$options":"-i"}},
                {"shortcategory":{"$regex":str(acode),"$options":"-i"}},
                ]
            result = collection.find({'$and':myConditions},{"_id":False})
            # result = collection.find()
            result = dumps(result)
            logging.info(len(result))

        except Exception as e:
            result="[{'Error':'No Result by "+str(code)+ "code. Enter numerical value. Example: code=12345'}]"
            logging.info("Error below:")
            logging.info(e)
        if len(result)==2:
            result="[{'Error':'No Result by that code "+str(code)+". Enter numerical value. Example: code=12345'}]"
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)