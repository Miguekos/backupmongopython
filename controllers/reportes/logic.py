#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pandas
import time

class ReporteProcess:
    def __init__(self, object):
        print("object", object)
        self.IP = object['ip'] # "192.168.44.72"
        self.PORT = object['port'] # 27017
        self.ADMIN = object['user']
        self.PASSWORD = object['password']
        self.db = object['db']
        self.collection = object['collection']
        self.nombre_del_reporte = object['namereport']
        self.query = object['query']
        self.projection = object['projection']

    def inicio(self):
        # build a new client instance of MongoClient
        mongo_client = MongoClient(self.IP, self.PORT, username=self.ADMIN, password=self.PASSWORD)

        db = mongo_client[self.db]
        col = db[self.collection]

        # start time of script
        start_time = time.time()

        # make an API call to the MongoDB server
        cursor = col.find(self.query).projection(self.projection)

        # extract the list of documents from cursor obj
        mongo_docs = list(cursor)

        # restrict the number of docs to export
        mongo_docs = mongo_docs[:]  # slice the list
        print("total docs:", len(mongo_docs))

        # create an empty DataFrame for storing documents
        docs = pandas.DataFrame(columns=[])

        # iterate over the list of MongoDB dict documents
        for num, doc in enumerate(mongo_docs):
            # convert ObjectId() to str
            doc["_id"] = str(doc["_id"])

            # get document _id from dict
            doc_id = doc["_id"]

            # create a Series obj from the MongoDB dict
            series_obj = pandas.Series(doc, name=doc_id)

            # append the MongoDB Series obj to the DataFrame obj
            docs = docs.append(series_obj)

            # only print every 10th document
            if num % 10 == 0:
                print(type(doc))
                print(type(doc["_id"]))
                print(num, "--", doc, "\n")

        """
        EXPORTAR LOS DOCUMENTOS DEL MONGODB
        EN DIFERENTES FORMATOS
        """
        # print("\nexporting Pandas objects to different file types.")
        print("\nCantidad de DataFrame (len):", len(docs))

        ruta = "./tmp/{}".format(self.nombre_del_reporte)

        try:
            import os
            os.mkdir(ruta)
        except OSError:
            print("La creación del directorio %s falló" % ruta)
        else:
            print("Se ha creado el directorio: %s " % ruta)

        # export the MongoDB documents as a JSON file
        docs.to_json("{}/{}.json".format(ruta, self.nombre_del_reporte))

        # have Pandas return a JSON string of the documents
        json_export = docs.to_json()  # return JSON data
        print("\nJSON data:", json_export)

        # export MongoDB documents to a CSV file
        docs.to_csv("{}/{}.csv".format(ruta, self.nombre_del_reporte), ",")  # CSV delimited by commas

        # export MongoDB documents to CSV
        csv_export = docs.to_csv(sep=",")  # CSV delimited by commas
        print("\nCSV data:", csv_export)

        # create IO HTML string
        import io

        html_str = io.StringIO()

        # export as HTML
        docs.to_html(
            buf=html_str,
            classes='table table-striped'
        )

        # print out the HTML table
        print(html_str.getvalue())

        # save the MongoDB documents as an HTML table
        docs.to_html("{}/{}.html".format(ruta, self.nombre_del_reporte))

        print("\n\ntime elapsed:", time.time() - start_time)

        import os
        import glob
        import csv
        import xlwt  # from http://www.python-excel.org/
        # from config import *

        # ifile  = open('sample.csv', "rt", encoding=<theencodingofthefile>)

        def ConvertirEnviar(name):
            try:
                print('{}.csv'.format(name))
                for csvfile in glob.glob(os.path.join('.', '{}/{}.csv'.format(ruta, name))):
                    print("csvfile", csvfile)
                    wb = xlwt.Workbook()
                    ws = wb.add_sheet('data')
                    with open(csvfile, 'rt', encoding="utf8") as f:
                        reader = csv.reader(f)
                        for r, row in enumerate(reader):
                            # print(row)
                            for c, val in enumerate(row):
                                ws.write(r, c, val)
                    wb.save("{}/{}.xls".format(ruta, self.nombre_del_reporte))
                    os.remove(csvfile)
                return True
            except:
                return False

        ConvertirEnviar("{}".format(self.nombre_del_reporte))

        return "{}".format(self.nombre_del_reporte)
