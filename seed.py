"""Script to seed a database"""

import os

import crud
import model 
import os

import csv

import server
from faker import Faker

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
        print(row['name'])
        print(row['seller_id'])
        print(row['winner_id'])
        end_date_test = row['end_date']
        print(row['end_date'])
        print(row['description'])
        print(row['melon_category'])
        print(ast.literal_eval(row['is_sold']))
        #crud.create_melon_listing(row['name'], row['seller_id'], row['winner_id'])