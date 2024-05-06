import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps
import certifi
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python getPosts trigger function processed a request.')
    try:
        url = os.environ["DB_CONNECTION"]
        client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
        database = client['vytt1-db']
        collection = database['posts']
        result = collection.find({})
        result = dumps(result)
        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)