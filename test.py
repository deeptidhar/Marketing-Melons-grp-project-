"""Testing flask routes and database in server.py"""

from unittest import TestCase
from flask import *
from server import *
from model import *
import crud
import sys
import os


   
class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///test_db")

        # Create tables and add sample data
        db.create_all()

        self.user = crud.create_user(email='LJohnson234@yahoo.com', password ='Uy8N96xD', name ='Lamont Johnson')

        
    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        
        
    def test_user_creation(self):
        """Test user profile page and to make sure user object 
        has been created successfully"""
        
        self.assertIsInstance(self.user, User)
        
    def test_email(self):
        """Testing that the user object 'email' 
        has been constructed properly"""
        
        self.assertEqual('LJohnson234@yahoo.com', self.user.email)



           
if __name__ == "__main__":
    
    connect_to_db(app)
    
    import unittest

    unittest.main()