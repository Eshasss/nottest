#never mention this stuff

from sqlalchemy.orm import Session
from db_init import engine, User, Token


session = Session(engine)

user1 = User(
    name="shs",
    password = "bulbulbul",
    tokens=[Token(token="supertoken")],
)
query = session.query(User).filter(User.name=="shs")

session.add(user1) 
print("Эаовшоашвоа",query)
session.commit()