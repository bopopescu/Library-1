from flask import Flask, jsonify
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



@app.route('/library/api/v1.0/tasks/', methods=['GET'])
def get_all_books():
    if test_connection():
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(dictionary=True)
        query = "SELECT title, author FROM library"
        cursor.execute(query)
        books = []
        for row in cursor:
            print("* {title}: {author}".format(**row))
            books.append(row)
    return jsonify({'books': books})





if __name__ == '__main__':
    app.run(debug=True)
