import psycopg2
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import pandas as pd

DB_NAME = "anicybqt"
DB_USER = "anicybqt"
DB_PASS = "lZ3dcF3RsHvdd-cFVN2LHszOUhWweASb"
DB_HOST = "rogue.db.elephantsql.com"
DB_PORT = "5432"

app = Flask(__name__)
api = Api(app)

#def CreateConnection():
try:
    connector = psycopg2.connect(database = DB_NAME,
                                user = DB_USER,
                                password= DB_PASS,
                                host= DB_HOST,
                                port = DB_PORT)
    
except:
    connector = 0

class ItemsDB(Resource):
    def get(self, item_id):
        return pd.read_sql_query("""
            Select Items.content from Items where Items.item_id = %d
            """ % item_id, connector)["content"].to_json()
        

api.add_resource(ItemsDB,'/ItemsDB/<int:item_id>')

if __name__ == "__main__":
    if connector != 0:
        app.run(debug = True)
