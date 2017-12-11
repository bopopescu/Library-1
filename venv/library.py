from flask import Flask, jsonify, current_app, abort
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)


config = {'user': 'root',
          'password': 'kennedy',
          'host': '127.0.0.1',
          'database': 'Library'}


def test_connection():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Invalid Username or Password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    return True


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
        return jsonify({'entries': books})

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




if __name__ == '__main__':
    app.run(port=5000, debug=True)
