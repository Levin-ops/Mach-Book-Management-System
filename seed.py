from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book, Base


engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
   
    author1 = Author(author_name="J.K. Rowling", contact_info="contact@example.com", nationality="British", genres_published="Fantasy")
    author2 = Author(author_name="Stephen King", contact_info="contact@example.com", nationality="American", genres_published="Horror")
    author3 = Author(author_name="Agatha Christie", contact_info="contact@example.com", nationality="British", genres_published="Mystery")


    book1 = Book(book_title="Harry Potter and the Philosopher's Stone", book_genre="Fantasy", book_status="New", author=author1)
    book2 = Book(book_title="The Shining", book_genre="Horror", book_status="New", author=author2)
    book3 = Book(book_title="Murder on the Orient Express", book_genre="Mystery", book_status="New", author=author3)
    book4 = Book(book_title="The Hobbit", book_genre="Fantasy", book_status="New", author=author1)
   
    session.add_all([author1, author2,author3, book1, book2, book3, book4])


    session.commit()
    print("Data seeded successfully.")

if __name__ == "__main__":
    Base.metadata.create_all(engine) 
    seed_data()  