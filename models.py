from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base


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


class Author(Base):

    __tablename__ = 'authors'

    id = Column(Integer, primary_key= True)
    author_name = Column(String)
    contact_info = Column(String)
    nationality = Column(String)
    genres_published = Column(String)

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key= True)
    book_title = Column(String, nullable= False)
    book_genre = Column(String, nullable= False)
    book_author = Column(String, ForeignKey('authors.id'))
    book_status = Column(String)