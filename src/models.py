import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(120), nullable=False)
    login = Column(Boolean)
    
class Follower(Base):
    __tablename__ = 'follower'

    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'
    
    id = Column(Integer, primary_key=True)
    comment_text = Column(Text())
    author_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    created_at = Column(DateTime)

    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    url = Column(String)
    # type_of_media = Column() how to make this an enum???


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e