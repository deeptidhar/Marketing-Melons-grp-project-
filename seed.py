"""Script to seed a database"""

import os

import crud
import model 
import os

# import server
from faker import Faker

os.system('dropdb marketplace')
os.system('createdb marketplace')

model.connect_to_db(server.app)
model.db.create_all()

faker = Faker()
for _ in range(20): #can you do `for i in range(20)`?
    email = faker.email()
    password = faker.password()
    name = faker.name()
    print(email, password, name)
    crud.create_user(email, password, name)