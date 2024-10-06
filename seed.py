from app import app, db
from models import Book

# Data to seed
books = [
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Romance"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic"},
    {"title": "Moby Dick", "author": "Herman Melville", "genre": "Adventure"}
]

# Seed function to add books to the database
def seed_data():
    with app.app_context():  
        db.drop_all()        
        db.create_all()      

        # Iterate through the book data and insert into the database
        for book_data in books:
            book = Book(
                title=book_data["title"],
                author=book_data["author"],
                genre=book_data["genre"]
            )
            db.session.add(book)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_data()
