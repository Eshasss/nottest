#eto chenovbyk on potom propadet chestno
from sqlalchemy.orm import Session
from db_init import engine, User

session = Session(engine)

user3 = User(name="Eshas", password="NotEshas")
session.add_all([user3])
session.commit()

session.close()
PYTHONPATH=./src/db_manager

https://i.pinimg.com/736x/22/50/1d/22501dfc2b2911601676ef23ca06a080.jpg