import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
from bson.objectid import ObjectId
import logging
import certifi
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    if id:
        try:
            url = os.environ["DB_CONNECTION"]
            client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
            database = client['vytt1-db']
            collection = database['advertisements']
            query = {'_id': id}
            result = collection.find_one(query)
            print("----------result--------")
            result = dumps(result)
            print(result)
            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except:
            return func.HttpResponse("Database connection error.", status_code=500)
    else:
        return func.HttpResponse("Please pass an id parameter in the query string.", status_code=400)