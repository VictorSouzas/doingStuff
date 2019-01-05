from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """User Model."""

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String)
    fullname = db.Column(db.String)
    password = db.Column(db.String)

    def get_user_id(self):
        """Return self.id."""
        return self.id

    def validate_password(self, password):
        """Return bollean."""
        return self.password == password
