from flask import Flask, request, jsonify, make_response
from flask_migrate import Migrate
from models import db, Book
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return 'Welcome to the Flask App!'

# PATCH Method to update book data
@app.route('/books/<int:id>', methods=['PATCH'])
def update_book(id):
    book = Book.query.get_or_404(id)
    data = request.get_json()

    if 'title' in data:
        book.title = data['title']
    if 'author' in data:
        book.author = data['author']
    if 'genre' in data:
        book.genre = data['genre']

    db.session.commit()

    response_body = {
        'message': 'Book updated successfully',
        'book': book.to_dict()
    }
    return make_response(jsonify(response_body), 200)

# DELETE Method to remove a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify({'message': 'Book deleted successfully'}), 200)

# Helper route to create new book (POST)
@app.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], genre=data['genre'])

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(new_book.to_dict()), 201)

# Helper route to fetch all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    books_list = [book.to_dict() for book in books]

    return make_response(jsonify(books_list), 200)

if __name__ == '__main__':
    app.run(port=5554,debug=True)
