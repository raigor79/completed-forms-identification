import collections
from re import TEMPLATE
from pymongo import MongoClient
import pprint

TEMPLATE_FORM = {
    "name": 'name'
}


if __name__ == "__main__":

    client = MongoClient("mongodb://172.24.0.1:27017")
    db = client.dbforms
    collections = db.typeforms
    # form_id = collections.insert_one({
    #     "name": "UserForm",
    #     "phone": "phone",
    #     "e_mail": "mail"   
    # })
    for i in collections.find():
     pprint.pprint(i)


    