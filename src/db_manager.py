from sqlalchemy.orm import Session
from .db_init import engine, User
from sqlalchemy import select
from sqlalchemy.sql import exists


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
    
    # if not login_check:
    #     session.add(User(name =data["name"], password = data["password"]))
    #     session.commit()
    #     return True
    # else: 
    #     return False
    session.add(User(name =data["name"], password = data["password"]))
    session.commit()
    return True

def delete_user(uid):
    """
    Deletes the user
    """
    User.query.filter(User.id == uid).delete()
    session.commit()



def login_check(data):
    """
    Checks is the password and token correct and is user corrently online
    True - already registered
    False - Not registered   /sth is wrong
    """
    if user_exist(data):
        query = session.query(User).filter(
            User.name==data["name"] 
            & User.password==data["password"]).scalar()
        return query
    else:
        return "Wrong password"
def change_password():
    """
    Changes the password password
    """
    pass
