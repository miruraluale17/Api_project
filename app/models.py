from sqlalchemy import Column, INTEGER, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.elements import False_
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP, Integer
from .database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(INTEGER, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(INTEGER, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id = Column(INTEGER, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    phone_munber = Column(INTEGER)

class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(INTEGER, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    post_id = Column(INTEGER, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)