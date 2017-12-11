from flask import Flask, jsonify, current_app, abort
from flask_restful import Resource, Api
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)
api = Api(app)


config = {'user': 'root',
          'password': 'kennedy',
          'host': '127.0.0.1',
          'database': 'Library'}

class HelloWorld(Resource):
    def get(self):
        return get_entries

class get_entries():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT * from library"
    cursor.execute(query)


class Library(Resource):
    def get(self, book_id):
        return {book_id: entries[book_id]}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)



