from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable= False)
    password = Column(String, nullable= False)
    genre_preference = Column(String)
    created = Column(DateTime, default= datetime.utcnow)

    def __repr__(self):
        return(
            f"User(id ={self.id})"
            + f"first_name = {self.first_name}"
            + f"last_name = {self.last_name}"
            )



class Author(Base):

    __tablename__ = 'authors'

    id = Column(Integer, primary_key= True)
    author_name = Column(String)
    contact_info = Column(String)
    nationality = Column(String)
    genres_published = Column(String)
    books = relationship('Book', back_populates='author')

    def __repr__(self):
        return(
            f"Author(id ={self.id})"
            + f"author_name = {self.author_name}"
            + f"contact_info = {self.contact_info}"
            + f"nationality = {self.nationality}"
            )
    

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key= True)
    book_title = Column(String, nullable= False)
    book_genre = Column(String, nullable= False)
    book_status = Column(String)
    book_author = Column(Integer, ForeignKey('authors.id'))
    author = relationship('Author', back_populates='books')
    reviews = relationship("Review", back_populates="book")

    def __repr__(self):
        return(
            f"Book(id ={self.id})"
            + f"Book_Title = {self.book_title}"
            + f"Book_Author = {self.author.author_name if self.author else None}"
            + f"Book_Genre = {self.book_genre}"
            )

class Review(Base):

    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True)
    review_text = Column(String)
    book_id = Column(Integer, ForeignKey("books.id"))

    book = relationship('Book', back_populates="reviews")

    def __repr__(self):
        return(
            f"Review(id ={self.id})"
            + f"Review = {self.review_text}"
            )


