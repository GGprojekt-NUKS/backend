from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# insert initial data
sports = Topics(topic='sports')
food = Topics(topic='food')
politics = Topics(topic='politics')
health = Topics(topic='health')
tourism = Topics(topic='tourism')

session.add_all([sports, food, politics, health, tourism])
session.commit()

session.close()