from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///forum.db")

Base = declarative_base()

class Forum(Base):
    __tablename__ = "texts"

    id = Column(Integer, primary_key=True)
    text = Column(String(50))
    topic_id = Column(Integer, ForeignKey("topics.id"))

    topic = relationship("Topics", back_populates="forum_topics")

class Topics(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    topic = Column(String(50), nullable=False)

    forum_topics = relationship("Forum", back_populates="topic")




