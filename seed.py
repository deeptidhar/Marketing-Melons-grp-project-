"""Script to seed a database"""

import os

import crud
import model 
import os

import csv

import server
from faker import Faker

os.system('dropdb marketplace')
os.system('createdb marketplace')

model.connect_to_db(server.app)
model.db.create_all()

faker = Faker()
for _ in range(20):
    email = faker.email()
    password = faker.password()
    name = faker.name()
    crud.create_user(email, password, name)
 
with open('melon_categories.csv', newline='') as categories_csv:
    categories_reader = csv.DictReader(categories_csv)
    for row in categories_reader:
        crud.create_melon_category(row['is_seedless'], row['name'], row['color'], row['melon_img_url'])
