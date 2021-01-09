from os.path import join
import pymongo
from bson.json_util import dumps, JSONOptions, DatetimeRepresentation
# from bson.json_util import load
import json
import os
import shutil
import datetime


def slice(sourcedict, string):
    for key in sourcedict.keys():
        if key.startswith(string) and key.endswith(string):
            del sourcedict[key]
    return sourcedict


def listar_db(backup):
    # client = pymongo.MongoClient("'192.168.44.72', 27017")
    try:
        client = pymongo.MongoClient(
            "mongodb://{}:{}@{}:{}".format(backup["user"], backup["password"], backup["ip"], backup["port"]))
    except:
        client = pymongo.MongoClient("mongodb://{}:{}".format(backup["ip"], backup["port"]))
    db = client.list_database_names()
    print(db)
    return db


def backup_db(backup):
    try:
        client = pymongo.MongoClient(
            "mongodb://{}:{}@{}:{}".format(backup["user"], backup["password"], backup["ip"], backup["port"]))
        database = client['{}'.format(backup["db"])]
    except:
        client = pymongo.MongoClient(
            "mongodb://{}:{}".format(backup["ip"], backup["port"]))
        database = client['{}'.format(backup["db"])]

    try:
        os.mkdir("./dbs/{}".format(backup["db"]))
    except:
        pass
    # authenticated = database.authenticate(<uname>,<pwd>)
    # assert authenticated, "Could not authenticate to database!"
    collections = database.collection_names()
    for i, collection_name in enumerate(collections):
        col = getattr(database, collections[i])
        # collection = col.find()
        json_options = JSONOptions(datetime_representation=DatetimeRepresentation.ISO8601)
        temp_filepath = "{}/{}.json".format("./dbs/{}".format(backup["db"]), collection_name)
        # for collection_name in database.collection_names():
        with open(temp_filepath, "w") as f:
            for doc in database.get_collection(collection_name).find():
                f.write(dumps(doc, json_options=json_options) + "\n")
    fecha = datetime.datetime.now().strftime("%Y_%m_%d")
    shutil.make_archive("./tmp/{}_{}".format(backup["db"], fecha), 'zip', "./dbs/{}".format(backup["db"]))


def restore_db(backup_file):
    client = pymongo.MongoClient()
    database = client.Retrive
    retrived = database['retrived']
    with open(backup_file, 'r') as file:
        data = json.loads(file.read())
        for i in range(len(data)):
            '''
            Ingoring Random _id which contains special charactors which are not supported to insert in database
            If you have manually added your _id field then ignore slicing
            '''
            x = slice(data[i], "_id")
            post_id = retrived.insert(data[i])

# backup_db("./EncuestasATV")
# restore_db("./")
