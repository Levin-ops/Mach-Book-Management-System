from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///library.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable= False)
    password = Column(String, nullable= False)
    genre_preference = Column(String)
    created = Column(DateTime, default= datetime.utcnow)
    borrowed_books = relationship('Book', back_populates= 'borrower')

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

    def add_genre(self, genre):
        if not self.genres_published:
            self.genres_published = f"[{genre}]"
        else:
            genres_list = eval(self.genres_published)
            if genre not in genres_list:
                genres_list.append(genre)
                self.genres_published = str(genres_list)

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
    borrower_id = Column(Integer, ForeignKey('users.id'))
    borrower = relationship('User', back_populates='borrowed_books')

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


if __name__ == "__main__":
    Base.metadata.create_all(engine)