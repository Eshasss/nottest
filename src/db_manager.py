from sqlalchemy.orm import Session
from .db_init import engine, User, Token
from sqlalchemy import select
from sqlalchemy.sql import exists
import uuid
 
#тут путаница с функцией в функции в которой функции берегите глаза пожалуйста!

session = Session(engine)

def user_exist(data):
    """
    Checks does the login exist
    True - Exists
    False - Nope
    """
    return session.query(exists().where(User.name==data["name"])).scalar()
    

def add_user(data):

    """
    Add user to database
    True - create
    False - already exists
    """
    new_token = str(uuid.uuid4())
    
    session.add(User(name =data["name"], 
                    password = data["password"],
                    tokens=[Token(token=new_token)]))
    session.commit()


def get_token_by_name(data):
    id_query = session.query(User).filter(User.name==data["name"])
    myid = id_query.one().id
    token_query = session.query(Token).filter(Token.user_id==myid)
    mytoken = token_query.one().token
    return mytoken
    

def login_user(data):
    if is_logged:
        new_token = str(uuid.uuid4())
        id_query = session.query(User).filter(User.name==data["name"])

        myid = id_query.one().id

        token_query = session.query(User).filter(Token.user_id==myid)
        token_query.token = new_token
        #все верно ура
        return True
    else:
        #дэмн 
        return False


def is_logged(data):
    mytoken = get_token_by_name(data)
    if mytoken == "":
        #не онлайн
        return True
    else:
        #онлайн
        return False
    

def logout(data):
    id_query = session.query(User).filter(User.name==data["name"])
    myid = id_query.id
    token_query = session.query(User).filter(Token.user_id==myid)
    token_query.token = ""
    session.commit()
    
    

def delete_user(data):
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
            & (User.password==data["password"])
            )).scalar()
    return query

def change_password():
    """
    Changes the password password
    """
    pass
