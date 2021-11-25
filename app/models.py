from sqlalchemy.orm import deferred, relationship
from sqlalchemy import Column
from sqlalchemy.sql.expression import false, null, text, true
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer,String, Boolean
from sqlalchemy.sql.visitors import TraversibleType
from .database import Base

class Post(Base):
    __tablename__="posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),nullable=False)
    
    owner=relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Vote(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey(
        "users.id",ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey(
        "posts.id",ondelete="CASCADE"),primary_key=True)