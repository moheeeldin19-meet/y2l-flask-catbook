from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db', connect_args={'check_same_thread': False})
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name,vote):
    cat_object = Cat(name=name,vote=vote)
    session.add(cat_object)
    session.commit()
    return cat_object

def get_all_cats():
    cats = session.query(Cat).all()
    return cats
def get_cat(id):
	cat=session.query(Cat).filter_by(id=id).first()
	return cat