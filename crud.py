"""CRUD operations"""

from model import *
from flask_sqlalchemy import SQLAlchemy

def create_user(email, password, name):
    """Create new user"""

    user = User(email = email, password = password, name = name)
    db.session.add(user)
    db.session.commit()

    return user


def get_users():
    """Get all users"""
    
    return User.query.all()


def get_user_by_id(user_id):
    """Find a user using id"""

    return User.query.get(user_id)


def get_user_by_email(email):
    """Find a user using email"""

    return User.query.filter(User.email == email).first()


def create_melon_category(is_seedless, name, color, melon_img_url):
    """Create a new melon category"""
    
    melon_category = MelonCategory(is_seedless = is_seedless, name = name, color = color, melon_img_url = melon_img_url)
    db.session.add(melon_category)
    db.session.commit()

    return melon_category


def get_melon_categories():
    """Get all melon categories"""

    return MelonCategory.query.all()


def get_category_by_id(category_id):
    """Get a melon category using id"""

    return MelonCategory.query.get(category_id)


def create_melon_listing(name, seller_id, winner_id, end_date, description, melon_category, is_sold):
    """Create a new melon listing"""

    melon_listing = Melon(name = name, seller_id = seller_id, winner_id = winner_id, end_date = end_date, description = description, melon_category = melon_category, is_sold = is_sold)
    db.session.add(melon_listing)
    db.session.commit()

    return melon_listing


def get_melon_listings():
    """Get all melon listings"""

    return Melon.query.all()


def get_melon_by_id(melon_id):
    """Get melon listing using id"""

    return Melon.query.get(melon_id)


def create_bid(user_id, melon_id, bid_amount, timestamp):
    """Create a new bid"""

    bid = Bid(user_id = user_id, melon_id = melon_id, bid_amount = bid_amount, timestamp = timestamp)
    db.session.add(bid)
    db.session.commit()

    return bid


def get_all_bids():
    """Get all bids"""

    return Bid.query.all()


def get_bid_by_id(bid_id):
    """Get a bid using id"""

    return Bid.query.get(bid_id)




