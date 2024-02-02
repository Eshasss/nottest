from sqlalchemy.orm import Session
from .db_init import engine, User
from sqlalchemy import select


session = Session(engine)

def user_exist(user):
    """
    Checks does the login exist
    """
    pass

def add_user(user: User):

    """
    Add user to database
    """
    session.add(user)
    session.commit()
    return user.uid

def delete_user(uid):
    """
    Deletes the user
    """
    User.query.filter(User.id == uid).delete()
    session.commit()



def login_check():
    """
    Checks is the password and token correct
    """
    pass

def change_password():
    """
    Changes the password password
    """
