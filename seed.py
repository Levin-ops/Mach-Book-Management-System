from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, Book, Base


engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

def seed_data():
   
    author1 = Author(author_name="J.K. Rowling", contact_info="contact@example.com", nationality="British", genres_published="")
    author2 = Author(author_name="Stephen King", contact_info="contact@example.com", nationality="American", genres_published="")
    author3 = Author(author_name="Agatha Christie", contact_info="contact@example.com", nationality="British", genres_published="")
    author4 = Author(author_name="Harper Lee", contact_info="contact@example.com", nationality="American", genres_published="")
    author5 = Author(author_name="George Orwell", contact_info="contact@example.com", nationality="British", genres_published="")
    author6 = Author(author_name="Leo Tolstoy", contact_info="contact@example.com", nationality="Russian", genres_published="")
    author7 = Author(author_name="Mark Twain", contact_info="contact@example.com", nationality="American", genres_published="")
    author8 = Author(author_name="F. Scott Fitzgerald", contact_info="contact@example.com", nationality="American", genres_published="")
    author9 = Author(author_name="Charles Dickens", contact_info="contact@example.com", nationality="British", genres_published="")
    author10 = Author(author_name="Ernest Hemingway", contact_info="contact@example.com", nationality="American", genres_published="")

    book1 = Book(book_title="Harry Potter and the Philosopher's Stone", book_genre="Fantasy", book_status="Available", author=author1)
    book2 = Book(book_title="The Shining", book_genre="Horror", book_status="Available", author=author2)
    book3 = Book(book_title="Murder on the Orient Express", book_genre="Mystery", book_status="Available", author=author3)
    book4 = Book(book_title="To Kill a Mockingbird", book_genre="Drama", book_status="Available", author=author4)
    book5 = Book(book_title="1984", book_genre="Dystopian", book_status="Available", author=author5)
    book6 = Book(book_title="War and Peace", book_genre="Historical Fiction", book_status="Available", author=author6)
    book7 = Book(book_title="Adventures of Huckleberry Finn", book_genre="Adventure", book_status="Available", author=author7)
    book8 = Book(book_title="The Great Gatsby", book_genre="Classic", book_status="Available", author=author8)
    book9 = Book(book_title="Great Expectations", book_genre="Classic", book_status="Available", author=author9)
    book10 = Book(book_title="The Old Man and the Sea", book_genre="Literary Fiction", book_status="Available", author=author10)

    session.add_all([author1, author2, author3, author4, author5, author6, author7, author8, author9, author10,
                     book1, book2, book3, book4, book5, book6, book7, book8, book9, book10])


    session.commit()
    print("Data seeded successfully.")

if __name__ == "__main__":
    Base.metadata.create_all(engine) 
    seed_data()  