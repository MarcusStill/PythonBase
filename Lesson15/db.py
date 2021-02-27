from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
engine = create_engine('mysql://frankenstein:X4a2N8v91290$@149.202.217.219/lesson_db', echo=True)