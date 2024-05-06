import azure.functions as func
import pymongo
from bson.objectid import ObjectId
import certifi
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    id = req.params.get('id')
    request = req.get_json()
    if request:
        try:
            url = os.environ["DB_CONNECTION"]
            client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
            database = client['vytt1-db']
            collection = database['advertisements']
            filter_query = {'_id': id}
            update_query = {"$set": request}
            rec_id1 = collection.update_one(filter_query, update_query)
            return func.HttpResponse(status_code=200)
        except:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse('Please pass name in the body', status_code=400)

