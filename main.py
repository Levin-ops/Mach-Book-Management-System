from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

def register_user():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    genre_preference = input("Which Genre do you like? ")

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
        print(" Thank you for choosing Mach's Book Management System \n How can we be of help?")
        print("1. Search Books ")
        print("2. Display Books")
        print("3. Leave a Review")
        print("4. Logout")

        choice = input("Enter your Selection: ")

        

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
                print("Login Successfull.")
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