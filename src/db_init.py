from sqlalchemy import create_engine, String, ForeignKey, Column, String, Integer, CHAR, Column  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "user_table"

    uid = Column(Integer, primary_key=True)
    name = Column("username", String)
    password = Column("password", String)

    def __init__(self, uid, name, password):
        self.uid = uid
        self.name = name
        self.password = password
    def __repr__(self) -> str:
        return f"{self.uid} {self.name} {self.password}"

engine = create_engine("sqlite:///test.db", echo = True)

Base.metadata.create_all(bind = engine)


