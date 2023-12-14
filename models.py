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

# author_book_association = Table(
#     "author_genre_association",
#     Base.metadata,
#     Column("author_id", Integer,ForeignKey('authors.id')),
#     Column('book_id', Integer, ForeignKey("book.id"))
# )
class Author(Base):

    __tablename__ = 'authors'

    id = Column(Integer, primary_key= True)
    author_name = Column(String)
    contact_info = Column(String)
    nationality = Column(String)
    genres_published = Column(String)

    def __repr__(self):
        return(
            f"Author(id ={self.id})"
            + f"author_name = {self.author_name}"
            + f"contact_info = {self.contact_info}"
            + f"nationality = {self.nationality}"
            )

# class Genre(Base):
#     __tablename__ = "genres"

#     id = Column(Integer, primary_key= True)
#     genre_name = Column(String)
#     authors = relationship("Author", secondary = author_genre_association, back_populates= "genres")
    
#     def __repr__(self):
#         return f"Genre(id={self.id}) genre_name={self.genre_name}"

class Book(Base):

    __tablename__ = 'books'

    id = Column(Integer, primary_key= True)
    book_title = Column(String, nullable= False)
    book_genre = Column(String, nullable= False)
    book_author = Column(String)
    book_status = Column(String)

    def __repr__(self):
        return(
            f"Book(id ={self.id})"
            + f"Book_Title = {self.book_title}"
            + f"Book_Author = {self.book_author}"
            + f"Book_Genre = {self.book_genre}"
            )




