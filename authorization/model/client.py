from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, ForeignKey, relationship
from authlib.flask.oauth2.sqla import OAuth2ClientMixin

Base = declarative_base()


class Client(Base, OAuth2ClientMixin):
    """Client Model."""

    __tablename__ = 'client'

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user = relationship('User')
