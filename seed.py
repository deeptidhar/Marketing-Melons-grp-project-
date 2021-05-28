"""Script to seed a database"""

import crud
from faker import Faker
import csv
from datetime import datetime, timedelta


def create_users():
    """Seeds User table"""
    # crud.create_user(email, password, name)
    faker = Faker()
    for _ in range(20):
        email = faker.email()
        password = faker.password()
        name = faker.name()
        crud.create_user(email, password, name)


def create_melon_categories():
    """Seeds MelonCategory table"""
    # create_melon_category(is_seedless, name, color, melon_img_url)
    with open('data/melon_categories.csv', newline='') as categories_csv:
        categories_reader = csv.DictReader(categories_csv)
        for row in categories_reader:
            crud.create_melon_category(eval(row['is_seedless']), 
                                       row['name'], 
                                       row['color'], 
                                       row['melon_img_url'])


def create_listings():
    """Seeds MelonListing table"""
    # create_melon_listing(name, seller_id, winner_id, end_date, description, melon_category, is_sold, start_price)
    with open('data/test_data_melon_listings.csv', newline='') as listings_csv:
        listings_reader = csv.DictReader(listings_csv)
        for row in listings_reader:
            print('*' * 25)
            print(row)
            crud.create_melon_listing(row['name'], 
                                    row['seller_id'], 
                                    eval(row['end_date']), 
                                    row['description'], 
                                    row['melon_category'],
                                    float(row['start_price']))


def create_bids():
    """Seeds Bid table"""
    with open('data/test_data_bids.csv', newline='') as bids_csv:
        bids_reader = csv.DictReader(bids_csv)
        for row in bids_reader:
            crud.create_bid(row['user_id'], 
                            row['melon_id'], 
                            row['bid_amount'], 
                            datetime.strptime(row['timestamp'], "%m/%d/%Y %H:%M:%S"))


def create_example_data():
    create_users()
    create_melon_categories()
    create_listings()
    create_bids()


if __name__ == '__main__':
    import argparse
    import os
    from model import db, connect_to_db
    from server import app
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', help='db to use', nargs="?", default='marketplace')
    args = parser.parse_args()
    selected_db = args.db
    print(selected_db)
    os.system(f'dropdb {selected_db} --if-exists')
    os.system(f'createdb {selected_db}')
    connect_to_db(app, f'postgresql:///{selected_db}')
    db.create_all()
    create_example_data()