from flask_sqlalchemy import SQLAlchemy
from authlib.flask.oauth2.sqla import OAuth2TokenMixin


db = SQLAlchemy()


class Token(db.Model, OAuth2TokenMixin):
    """Token Model."""

    __tablename__ = 'token'

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id',
                                                  ondelete='CASCADE'))
    user = db.relationship('User')

    def is_refresh_token(self):
        """pass."""
        pass
