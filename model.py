"""Models for Bits and Bytes of Melons Marketplace app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    bid = db.relationship('Bid', backref='users')
    # melons = db.relationship('Melon', backref='users')   # this was creating AmbiguousForeignKeysError; resolved with specifying foreign_keys argument
    melons = db.relationship('Melon', foreign_keys="Melon.seller_id")

    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.name} email={self.email}>'


class MelonCategory(db.Model):
    """A melon category."""

    __tablename__ = 'category'

    category_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    is_seedless = db.Column(db.Boolean)
    name = db.Column(db.String)
    color = db.Column(db.String)
    season = db.Column(db.String)

    def __repr__(self):
        return f'<Category category_id={self.category_id} name={self.name} seedless={self.is_seedless}>'


class Melon(db.Model):
    """Melon for sale in marketplace."""

    __tablename__ = 'melons'

    melon_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    name = db.Column(db.String)
    seller_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    winner_id = db.Column(db.Integer, db.ForeignKey('users.user_id')) 
    end_date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    melon_category = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    is_sold = db.Column(db.Boolean)

    def __repr__(self):
        return f'<Melon melon_id={self.melon_id} name={self.name} category={self.melon_category}>'


class Bid(db.Model):
    """A bid."""

    __tablename__ = 'bids'

    bid_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    melon_id = db.Column(db.Integer, db.ForeignKey('melons.melon_id'))
    bid_amount = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Bid bid_id={self.bid_id} User user_id={self.user_id} melon_id={self.melon_id} bid_amount={self.bid_amount}> timestamp={self.timestamp}>'


def connect_to_db(flask_app, db_uri='postgresql:///marketplace', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')


if __name__ == '__main__':
    pass
    # from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    # connect_to_db(app)