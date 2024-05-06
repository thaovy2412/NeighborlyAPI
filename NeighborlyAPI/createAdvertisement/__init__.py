import azure.functions as func
import pymongo
import certifi
import os

def main(req: func.HttpRequest) -> func.HttpResponse:
    request = req.get_json()
    if request:
        try:
            url = os.environ["DB_CONNECTION"]
            client = pymongo.MongoClient(url, tlsCAFile=certifi.where())
            database = client['vytt1-db']
            collection = database['advertisements']
            rec_id1 = collection.insert_one(request)
            return func.HttpResponse(req.get_body())
        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)
    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )