from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Author, User, Book, Base

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.create_all(engine)



def register_user():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    genre_preference = input("Which Genre do you prefer? ")

    user = User(first_name = first_name, last_name = last_name,email = email,
                password =password ,genre_preference = genre_preference)
    session.add(user)
    session.commit()
    print("Registration is Successfull.")

def authenticate_user(email,password):
    user = session.query(User).filter(User.email == email, User.password == password)
    return user

def after_login():
    while True:
        print("Thank you for choosing Mach's Book Management System \nHow can we be of help?")
        print("1. Search Books ", )
        print("2. Display Books")
        print("3. Donate Book")
        print("4. Leave a Review")
        print("5. Logout")

        choice = input("Enter your Selection: ")

        if choice == "1":
            search_books()
        elif choice == "2":
            display_books()
        elif choice == "3":
            donate_book()
        elif choice == "4":
            leave_a_review()
        elif choice == "5":
            print("Logging Out...")
            break
        else:
            print("Invalid Selection. Please Try Again.")


def donate_book():
    book_title = input("Enter Book Title: ")
    book_author_name = input("Enter Author Name: ")
    book_genre = input("Enter Book Genre: ")
    book_status = input("Enter Book Status (Old/New): ")
    
    author = session.query(Author).filter(Author.author_name == book_author_name).first()
    genre = session.query(Author).filter(Author.genres_published == book_genre)

    if author is None:
        author = Author(author_name = book_author_name)
        session.add(author)
        session.commit()

    book = Book(book_title = book_title, book_genre = book_genre,
                    book_status = book_status, author = author)
    
    session.add(book)
    session.commit()

    print("\nThank You For Your Donation.\n")

def search_books():
    search_term = input("Enter Book Title or Author's name to search: ")
    books = session.query(Book).filter(
    (Book.book_title.like(f"%{search_term}%")) |
    (Author.author_name.like(f"%{search_term}%"))).join(Author).all()

    if books:
        print("Search Results: ")
        for book in books:
            print(f"\nTitle: {book.book_title}\nAuthor:{book.author.author_name}\nGenre: {book.book_genre}\n")
    else:
        print("\nNo books found matching the search term.\n\n")


def display_books():
    books = session.query(Book).all()
    print("This is our Books Library:\nBooks: \n")
    
    for book in books:
        print(f"Title: {book.book_title}\nAuthor: {book.book_author} \nGenre: {book.book_genre}\n\n")


def leave_a_review():
    pass 

def main():
    while True:
        print("Welcome to Mach's Book Management System")
        print("1. New Member? Register")
        print("2. Login")
        print("00: Exit")

        choice = input("What is your selection? ")

        if choice == "1":
            register_user()
        elif choice == "2":
            email = input("Enter Email: ")
            password = input("Enter your password:")
            logged_in_user = authenticate_user(email,password)
            if logged_in_user:
                print("\n\n\nLogin Successfull.\n\n\n\n")
                after_login()
            else:
                print("Invalid email or password.")
        elif choice == "00":
            print("Exiting Application...")
            break
        else:
            print("Invalid Selection. Please Try Again.")


session.close()




if __name__ == "__main__":
    main()