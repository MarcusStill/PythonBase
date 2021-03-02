from sqlalchemy import create_engine, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("sqlite:///quote.db", echo=True)
Base = declarative_base(bind=engine)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, nullable=False, unique=True, autoincrement=True)
    name = Column(String(100), unique=True)


class Quote(Base):
    __tablename__ = 'quote'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    text = Column(String, nullable=True, unique=True)
    author_id = Column(Integer, ForeignKey('author.id'))
    created_at = Column(String)

    author = relationship("Author", backref="quotes")


def create_author(name: str) -> Author:
    new_author = Author(name=name)
    print("Id before", new_author.id)
    session.add(new_author)
    session.commit()
    print("Id after", new_author.id)
    return new_author


def create_quote(text: str, author_id: int, created_at: str) -> Quote:
    new_quote = Quote(text=text, author_id=author_id, created_at=created_at)
    print("id before", new_quote.id)
    session.add(new_quote)
    session.commit()
    print("id after", new_quote.id)
    return new_quote


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    session = Session()
    #new_author = create_author("Bob Marley")
    print("Print all Author")
    for instance in session.query(Author).order_by(Author.id):
        print("id", instance.id, instance.name)
    #new_quote = create_quote("Life is good", "1", "2021-03-02")
    #new_quote = create_quote("No Woman, no cry", "1", "2021-03-03")


    print("Print all quote one author")
    for instance in session.query(Quote).order_by(Quote.id):
        print("id", instance.id, instance.text, "author_id", instance.author_id, instance.created_at)


    print("Print all quotes one Author")
    query = session.query(Author, Quote)
    query = query.join(Quote, Quote.author_id == Author.id)
    records = query.all()
    print(records)
    for author, quote in records:
        print(author.name, "-", quote.text)


    session.close()

    """
    Добавление цитаты.
        - поиск в БД по номеру. Если цитата с таким номером есть  -->  не вносим.
        - если номера в БД нет --> Ищем автора. Если такой автор есть, то берем его номер и записываем цитату.
        - если автора нет  --> вносим автора, берем его номер и записываем цитату.
        
    """