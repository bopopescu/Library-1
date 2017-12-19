from flask import Flask, jsonify, current_app, abort, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String

import mysql.connector
from mysql.connector import errorcode
import datetime
import json
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kennedy'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+mysqlDB://localhost:5000/library'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

config = {'user': 'root',
          'password': 'kennedy',
          'host': '127.0.0.1',
          'database': 'Library'}

class Entry(db.Model):
    book_id = db.Column(db.Integer, primary_key=True, nullable=False)
    title = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    subtitle = db.Column(db.String(50))
    genre = db.Column(db.String(50))

def get_data():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT title, author, subtitle, genre, bookID FROM library"
    cursor.execute(query)
    books = []
    for row in cursor:
        books.append(row)
    with app.app_context():
        return json.dumps(books)

@app.route('/')
def index():
    return "Index - Starting Page of Jeremy's Webservice"


@app.route('/library/')
def library():
    return "This is the Library Page. \n\nOne day it may be a nice splash screen"


#Get all books
@app.route('/library/api/v1.0/books/', methods=['GET'])
def get_all_books():
    return get_data()

#Get books by bookID
@app.route('/library/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_a_book(book_id):
    data = get_data()
    book = [book for book in data if data['bookID'] == book_id]
    return jsonify({'book': book[0] })

#Get book by book title
@app.route('/library/api/v1.0/books/<string:book_title>', methods = ['GET'])
def get_data_by_title(book_title):
    r = requests.get()

#get boooks by author
@app.route('/library/api/v1.0/books/<string:author>', methods=['GET'])
def get_data_by_author(author):
    data = get_all_books
    book = [book for book in data if data['author'] == author]
    print(json.dumps(book))


#Add books to DB
@app.route('/library/api/v1.0/books', methods = ['POST'])
def create_entry():
    data = get_data()
    book = {'title' : request.json['title'],
            'author': request.json['author'],
            'subtitle' : request.json['subtitle'],
            'genre': request.json['genre']}
    return jsonify()




if __name__ == '__main__':
    app.run(port=5000, debug=True)
