from sqlalchemy.orm import Session
from .db_init import engine, User, Token
from sqlalchemy import select
from sqlalchemy.sql import exists
import uuid


session = Session(engine)

def user_exist(user):
    """
    Checks does the login exist
    True - Exists
    False - Nope
    """
    return session.query(exists().where(User.name=="name")).scalar()
    

def add_user(data):

    """
    Add user to database
    True - create
    False - already exists
    """
    new_token = uuid.uuid4()
    
    session.add(User(name =data["name"], 
                    password = data["password"],
                    tokens=[Token(token=new_token)]))
    session.commit()

def is_logged(data):
    query = session.query(User).filter(name =data["name"])
    myid = query.id
    token = session.query(User).filter(user_id=myid)
    mytoken = token.token
    if mytoken == "":
        return True
    else:
        return False
    

def logout(data):
    pass

def delete_user(uid):
    """
    Deletes the user
    """
    User.query.filter(User.id == uid).delete()
    session.commit()



def login_check(data):
    """
    Checks is the password and token correct and is user corrently online
    True - successs
    False - Not registered   /sth else is wrong
    """
    query = session.query(exists().where(
        (User.name==data["name"])
            & (User.password==data["password"]))).scalar()
    return query

def change_password():
    """
    Changes the password password
    """
    pass
