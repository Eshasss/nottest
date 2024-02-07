#never mention this stuff

from sqlalchemy.orm import Session
from db_init import engine, User, Token

from sqlalchemy.sql import exists
session = Session(engine)

# user1 = User(
#     name="Eshas",
#     password = "bulbulbul",
#     tokens=[Token(token="supertoken")],
# )
# query = session.query(exists().where(User.name=="memes")).scalar()
query = session.query(exists().where(
            (User.name=="Eshass")
            & (User.password=="bulbulbul"))).scalar()
# session.add(user1) 
print("ABABABABABBABABFISH",query)
session.commit()