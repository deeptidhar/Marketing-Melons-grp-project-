"""Script to seed a database"""

import os
import crud
import model 
import os
import server
from faker import Faker
import csv
import ast
from datetime import datetime

import ast #to convert "True" and "False" strings from the csv to boolean values

os.system('dropdb marketplace')
os.system('createdb marketplace')

model.connect_to_db(server.app)
model.db.create_all()

#seeds users table
faker = Faker()
for _ in range(20):
    email = faker.email()
    password = faker.password()
    name = faker.name()
    crud.create_user(email, password, name)
 
#seeds category table
with open('data/melon_categories.csv', newline='') as categories_csv:
    categories_reader = csv.DictReader(categories_csv)
    for row in categories_reader:
        crud.create_melon_category(ast.literal_eval(row['is_seedless']), row['name'], row['color'], row['melon_img_url'])

#seeds melon_listings table with test data
with open('data/test_data_melon_listings.csv', newline='') as listings_csv:
    listings_reader = csv.DictReader(listings_csv)
    for row in listings_reader:
        crud.create_melon_listing(row['name'], row['seller_id'], ast.literal_eval(row['winner_id']), datetime.strptime(row['end_date'], "%m/%d/%Y %H:%M:%S"), row['description'], row['melon_category'], ast.literal_eval(row['is_sold']))

#seeds bids table with test data
with open('data/test_data_bids.csv', newline='') as bids_csv:
    bids_reader = csv.DictReader(bids_csv)
    for row in bids_reader:
        crud.create_bid(row['user_id'], row['melon_id'], row['bid_amount'], datetime.strptime(row['timestamp'], "%m/%d/%Y %H:%M:%S"))
