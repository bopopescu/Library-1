from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:kennedy@localhost:3306/library"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class library(db.Model):
    __table__name = 'Library'
    id = db.Column('bookID',db.Integer, primary_key=True)
    title = db.Column('title',db.String(45), nullable=False)
    author = db.Column('author',db.String(45), nullable=False)
    date_obtained = db.Column('dateObtained',db.String(45),nullable=True)
    subtitle = db.Column('subtitle',db.String(45),nullable=True)
    finished = db.Column('finished',db.Integer)
    genre = db.Column('genre', db.String(45))

    # def __repr__(self):
    #     return "Library": {'title': self.title,
    #                         'subtitle': self.subtitle,
    #                         'author': self.author,
    #                         'genre': self.genre,
    #                         'dateObtained': self.date_obtained,
    #                         'finished:': self.finished}}

    def __init__(self, id, title, author, subtitle, genre, date_obtained, finished):
        self.id = id
        self.title = title
        self.author = author
        self.subtitle = subtitle
        self.genre = genre
        self.date_obtained = date_obtained
        self.finished = finished

    def _asdict(self):
        result = OrderedDict()
        for key in self.__mapper__.c.keys():
            result[key] = getattr(self, key)
        return result

    def serialize(self):
        return{
            'id' : self.id,
            'title' : self.title,
            'subtitle' : self.subtitle,
            'author' : self.author,
            'genre' : self.genre,
            'dateObtained' : self.date_obtained,
            'finished' : self.finished
        }

for books in library.query.all():
    print(library.serialize(books))



@app.route('/')
def index():
    return "Index Page - Welcome to Jeremy's Webservice"



@app.route('/library/api/v1.0/books/', methods = ['GET'])
def get_all_books():
    #https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask
    #Turning SQLALCHEMY into a JSON LIst.
    list_of_books = []
    for books in library.query.all():
        list_of_books.append(library.serialize(books))
    return jsonify(list_of_books)

@app.route('/library/api/v1.0/books/<string:author>', methods=['GET'])
def get_author_books():
    ouvre = ()
    for Library.author in Library:
       print(Library.author)
    return ouvre



if __name__ == '__main__':
    app.run(port=5000, debug=True)
