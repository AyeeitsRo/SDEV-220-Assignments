
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookdata.db'
db = SQLAlchemy(app)


class Books(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True, nullable = False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))
    
    def __repr__(self):
        return f"id {self.id}, name {self.name}, " + \
            f"author {self.author} publisher {self.publisher}"


@app.route('/')
def index():
    return 'Helloooo!'

@app.route('/books')
def get_books() -> str:
    books = Books.query.all()
    
    output = []
    for book in books:
        book_data = {
            'id': book.id,
            'name': book.name,
            'author': book.author,
            'publisher': book.publisher
        }
        
        output.append(book_data)
        
    return {'books': output}


@app.route('/books/<id>')
def get_book(id) -> str:
    book = Books.query.get_or_404(id)
    return {'id': book.id,
            'name': book.name,
            'author': book.author,
            'publisher': book.publisher
            }

@app.route('/books', methods=['POST'])
def add_book() -> str:
    book = Books()
    book.id = request.json["id"]
    book.name = request.json["name"]
    book.author = request.json["author"]
    book.publisher = request.json["publisher"]
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

app.route('/books/<id>', methods=['DELETE'])
def delete_book() -> str:
    book = Books.query.get(id)
    removed = book
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"Deleted Book:": removed}

app.route('/books/<id>', methods=['PUT'])
def update_book() -> str:
    book = Books.query.get_or_404(id)
    
    book.id = book.id
    book.name = request.json["name"]
    book.author = request.json["author"]
    book.publisher = request.json["publisher"]
    db.session.add(book)
    db.session.commit()

    return {'id': book.id,
            'name': book.name,
            'author': book.author,
            'publisher': book.publisher
            }