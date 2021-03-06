from flask_sqlalchemy import SQLAlchemy
from authlib.flask.oauth2.sqla import OAuth2ClientMixin

db = SQLAlchemy()


class Client(db.Model, OAuth2ClientMixin):
    """Client Model."""

    __tablename__ = 'client'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id',
                                                  ondelete='CASCADE'))
    user = db.relationship('User')
