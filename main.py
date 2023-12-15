from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Admin, Author,  Book, Base, Review, User

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

############ ADMIN FEATURES ############
def register_admin():
    username = input("Enter Prefered Username: ")
    password = input("Enter Password: ")

    admin = Admin(username = username, password =password)
    session.add(admin)
    session.commit()
    print("Admin Added.")



def admin_login():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        admin = authenticate_admin(username, password)

        if admin:
            print("\n\nLogin Successful.\n\n") 
            after_admin_login(admin)
            break
        else:
            print("Invalid username or password.")

def authenticate_admin(username, password):
    admin = session.query(Admin).filter(Admin.username == username, Admin.password == password).first()
    return admin

def after_admin_login(admin):
    while True:
        print("*"*10,"Mach's Book Management System\n")
        print("*"*20,"Admin")
        print("1. View Users.")
        print("2. Delete Users.")
        print("3. Add Book.")
        print("4. Delete Book.")
        print("0. Logout.")

        choice = input("Enter your Selection: ")

        if choice == "1":
            view_users()
        elif choice == "2":
            user_id = input("Enter User ID To DELETE: ")
            delete_user(user_id)
        elif choice == "3":
            add_book()
        elif choice == "4":
            book_title = input("Enter Book Title to delete: ")
            delete_book(book_title)
        elif choice == "0":
            print("Logging Out...")
            break
        else:
            print("Invalid Selection. Please Try Again.")

def view_users():
    users = session.query(User).all()
    for user in users:
        print(f"User ID: {user.id},\nName: {user.first_name} {user.last_name},\nEmail: {user.email}")

def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print(f"User with ID {user_id} has been deleted.")
    else:
        print("User not found.")

    print("====================================================")


def add_book():
    book_title = input("Enter Book Title: ")
    book_author_name = input("Enter Author Name: ")
    book_genre = input("Enter Book Genre: ")
    book_status = input("Enter Book Status (Available): ")
    
    author = session.query(Author).filter(Author.author_name == book_author_name).first()

    if author is None:
        author = Author(author_name = book_author_name)
        session.add(author)
        session.commit()

    book = Book(book_title = book_title, book_genre = book_genre,
                    book_status = book_status, author = author)
    
    session.add(book)
    session.commit()

    print("\nBook Added Successfully.\n")
    print("=====================================================")

def delete_book(book_title):
    book = session.query(Book).filter(Book.book_title.ilike(f"%{book_title}%")).first()
    if book:
        session.delete(book)
        session.commit()
        print(f"Book '{book_title}' has been deleted.")
    else:
        print("Book not found.")
    print("=====================================================")


############ USER FEATURES ############
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
    print("===============================================")

def login():
    while True:
        email = input("Enter Email: ")
        password = input("Enter Password: ")

        user = authenticate_user(email, password)

        if user:
            print("\n\nLogin Successful.\n\n")
            after_login(user) 
            break
        else:
            print("Invalid email or password.")
            register_option = input("Would you like to register? (yes/no): ").lower()
            if register_option == "yes":
                register_user()
                print("Registration successful. Please log in.")
            else:
                print("Returning to the main menu.")
            break
    print("==============================================")
def authenticate_user(email, password):
    user = session.query(User).filter(User.email == email, User.password == password).first()
    return user

def after_login(user):
    while True:
        print("*"*10,"Mach's Book Management System\n")
        print("*"*20,"User\n")
        print("1. Search Books ", )
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Donate Book")
        print("6. Leave a Review")
        print("98. Logout")

        choice = input("Enter your Selection: ")


        if choice == "1":
            search_books()
        elif choice == "2":
            display_books(user)
        elif choice == "3":
            borrow_book(user)
        elif choice == "4":
            return_book(user)
        elif choice == "5":
            donate_book()
        elif choice == "6":
            leave_a_review(user)
        elif choice == "98":
            print("Logging Out...")
            break
        else:
            print("Invalid Selection. Please Try Again.")
    print("==================================================")


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

    print("==================================================")


def display_books(user):
    books = session.query(Book).all()
    print("This is our Books Library:\nBooks: \n")
    
    for book in books:
        print(f"Title: {book.book_title}\nAuthor: {book.book_author} \nGenre: {book.book_genre}\n\n")

    borrow_option = input("Do you want to borrow any book from the library? (yes/no): ").lower()
    
    if borrow_option == "yes":
        borrow_book(user)


def borrow_book(user):
    book_title = input("Enter the title of the book you want to borrow: ")

    book = session.query(Book).filter(Book.book_title.ilike(f"%{book_title}%"), Book.book_status == "Available").first()

    if book:
        book.book_status = "Borrowed"
        book.borrower = user
        
        session.commit()
        print(f"You have successfully borrowed '{book.book_title}'.")
    else:
        print("Book not available.")

def return_book(user):
    book_title = input('Which Book are you returning? ')
    book = session.query(Book).filter(Book.book_title.ilike(f"%{book_title}%"), Book.borrower_id == user.id).first()

    if book:
        book.book_status = 'Available'
        book.borrower = None

        session.commit()
        print(f"You have successfully returned {book.book_title}.")
    else:
        print(f"Book not found in your record. ")

def donate_book():
    book_title = input("Enter Book Title: ")
    book_author_name = input("Enter Author Name: ")
    book_genre = input("Enter Book Genre: ")
    book_status = input("Enter Book Status (Available): ")
    
    author = session.query(Author).filter(Author.author_name == book_author_name).first()

    if author is None:
        author = Author(author_name = book_author_name)
        session.add(author)
        session.commit()

    book = Book(book_title = book_title, book_genre = book_genre,
                    book_status = book_status, author = author)
    
    session.add(book)
    session.commit()

    print("\nThank You For Your Donation.\n")


def leave_a_review(user):
    search_books()
    book_title = input("Enter Title of Book to Review: ")

    selected_book = session.query(Book).filter(Book.book_title.ilike(f"%{book_title}%")).first()

    if selected_book:
        review_text = input("Write your review for the book: ")

        review = Review(review_text = review_text, book = selected_book)
        session.add(review)
        session.commit()
        print("Your Review has been added. Thank you!")
    
    else:
        print("Book not found. Please enter a valid Book Title.")


def main():
    while True:
        print("Welcome to Mach's Book Management System")
        print("1. New Member? Register.")
        print("2. Login.")
        print("3. Admin Register.")
        print("4. Admin Log in.")
        print("00: Exit.")

        choice = input("What is your selection? ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login()
        elif choice =="3":
            register_admin()
        elif choice == "4":
            admin_login()
        elif choice == "00":
            print("Exiting Application...")
            break
        else:
            print("Invalid Selection. Please Try Again.")


session.close()


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    main()