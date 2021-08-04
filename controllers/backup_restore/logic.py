# from os.path import join
import pymongo
from bson.json_util import dumps, JSONOptions, DatetimeRepresentation, loads
# from bson.raw_bson import RawBSONDocument
# from bson.json_util import load
# import json
import os
import shutil
import datetime

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
iplocal = s.getsockname()[0]
# print("iplocal", iplocal)
s.close()

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
        if backup["user"] and backup["password"]:
            client = pymongo.MongoClient(
                "mongodb://{}:{}@{}:{}".format(backup["user"], backup["password"], backup["ip"], backup["port"]))
            database = client['{}'.format(backup["db"])]
        else:
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
        zipeando = shutil.make_archive("./tmp/{}_{}".format(backup["db"], fecha), 'zip', "./dbs/{}".format(backup["db"]))
        print("zipeando", zipeando)
        # return "http://95.111.235.214:3064/file/{}_{}.zip".format(backup["db"], fecha)
        return "http://{}:3064/file/{}_{}.zip".format(iplocal,backup["db"], fecha)
    except Exception as e:
        print("Exception", e)
        return e

def restore_db(backup):
    try:
        if backup["user_rest"] and backup["password_rest"]:
            client = pymongo.MongoClient(
                "mongodb://{}:{}@{}:{}".format(backup["user_rest"], backup["password_rest"], backup["ip_rest"], backup["port_rest"]))
        else:
            client = pymongo.MongoClient(
                "mongodb://{}:{}".format(backup["ip_rest"], backup["port_rest"]))
        database = client['{}'.format(backup["db_rest"])]
        collist = database.list_collection_names()
        carpeta_backup = "./dbs/{}".format(backup["db"])
        listar_archivos = os.listdir(carpeta_backup)
        print("listar_archivos", listar_archivos)
        for ar in listar_archivos:
            ruta = "./dbs/{}/{}".format(backup["db"], ar)
            collect = ar.split(".")[0]
            if collect != "system":
                mycol = database[collect]
                if collect in collist:
                    # print("The collection exists.")
                    return "The collection exists."
                else:
                    # print("collect", collect)
                    # print("ar", ruta)
                    # with open(ruta, 'r') as myfile:
                    # for line in open(ruta, 'r'):
                    try:
                        counter = 0
                        data = []
                        for num, h in enumerate(open(ruta, 'r')):
                            # print("num", num % 100)
                            h = loads(h)
                            data.append(h)
                            if num % 2000 == 0:
                                try:
                                    x = mycol.insert_many(data)
                                    counter = counter + len(x.inserted_ids)
                                    print("inserted_id", counter)
                                    data.clear()
                                except:
                                    pass
                        try:
                            x = mycol.insert_many(data)
                            print("inserted_id", counter + len(x.inserted_ids))
                        except:
                            pass
                    except Exception as e:
                        print("Exception", e)
                        return e
                    # print(data)
                        # else:
                        #     x = mycol.insert_many(data)
                        #     print("inserted_id", len(x.inserted_ids))
                        #     data.clear()
                        # data.append(h)
                        # for line in myfile:
                        #     # d = line.read().splitlines()
                        #     print(line.rstrip("\n"))
                        #     # if len(myfile) == 0:
                        #     #     print("collections {} empty".format(collect))
                        #     #     pass
                        #     # else:
                        #     # print("d",d)
                        #     data = []
                        #     for num, h in enumerate(myfile):
                        #         # print("h", type(h))
                        #         if num > 2000:
                        #             print("data_for_insert", data)
                        #         if num % 2000 == 0:
                        #             pass
                        #             # print("num", num)
                        #             # print("{} de la collections: {} -- y el doc es {} '\n'".format(num, collect, h))
                        #             # x = mycol.insert_many(data)
                        #             # print("inserted_id", len(x.inserted_ids))
                        #         h = loads(h.rstrip("\n"))
                        #         data.append(h)
                        #         # print(h)
                        #         # h['_id'] = str(h['_id']['$oid'])
                        #         # print("h", json.loads(h))
                        #     try:
                        #         print("fin")
                        #         # x = mycol.insert_many(data)
                        #         # print("inserted_id", len(x.inserted_ids))
                        #     except ValueError as e:
                        #         print("Exception", e)
                        #         return e
            else:
                print("collect", collect)
        return "Done"
    except ValueError as e:
        print("Exception", e)
        return e
