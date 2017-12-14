from flask import Flask, jsonify, current_app, abort, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
from mysql.connector import errorcode
import datetime
import json
import requests


app = Flask(__name__)
app.config['SECRET_KEY'] = 'kennedy'
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://localhost:5000/library'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

config = {'user': 'root',
          'password': 'kennedy',
          'host': '127.0.0.1',
          'database': 'Library'}



class Entry(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    genre = db.Column(db.String(50))




@app.route('/')
def index():
    return "Index - Starting Page of Jeremy's Webservice"


@app.route('/library/')
def library():
    return "This is the Library Page. \n\nOne day it may be a nice splash screen"


@app.route('/library/api/v1.0/books/', methods=['GET'])
def get_all_books():
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT title, author, subtitle, genre FROM library"
    cursor.execute(query)
    books = []
    for row in cursor:
            books.append(row)
    with app.app_context():
        return jsonify(books)

@app.route('/library/api/v1.0/books/<int:book_id>', methods=['GET'])
def get_a_book(book_id):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor(dictionary=True)
    query = "SELECT title, author, subtitle, genre FROM library WHERE bookID=" + str(book_id)
    cursor.execute(query)
    result = []
    for row in cursor:
        result.append(row)
    return jsonify({'book': result })


    #Will add goodreads score here
    #'goodreadsscore': var_name

@app.route('/library/api/v1.0/books', methods = ['POST'])
def create_entry():
    data = request.get_json()
    new_entry = Entry(author=data['author'], title = data['title'], subtitle = ['subtitle'], genre = data["genre"])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify()


#@app.route('/library/api/v1.0/books/<int:book_id', methods=['DELETE'])
#def delete_book(book_id):
#    book = [book for book in books if book['id'] == book_id]
#    if len(book) == 0:
#        abort(404)
#    books.remove(book[0])
#    return jsonify({'result': True})





if __name__ == '__main__':
    app.run(port=5000, debug=True)
