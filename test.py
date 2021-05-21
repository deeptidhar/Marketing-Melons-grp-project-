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

       # self.user = crud.create_user(email='LarryJackson278@yahoo.com', password ='SgK167xD', name ='Larry Jackson')
        #self.melon_category = crud.create_melon_category(is_seedless = False, name='Royal Golden Watermelon' , color='gold', melon_img_url='https://www.rareseeds.com/store/vegetables/watermelon/royal-golden-watermelon')
        self.melon_listing = crud.(name='', seller_id='', winner_id= '', end_date= '', description = 'One of the best', melon_category='', is_sold = False)
        #self.bid = crud.create_bid(user_id = 'users.user_id' , melon_id = '', bid_amount='9.50', timestamp='05/30/2021')

        
    def tearDown(self):
        """Do at end of every test."""

        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        
    ######################################################TESTING USER TABLE####################################################################    
    # def test_user_creation(self):
    #     """Test user profile page and to make sure user object 
    #     has been created successfully"""
        
    #     self.assertIsInstance(self.user, User)
        
    # def test_email(self):
    #     """Testing that the user object 'email' has been constructed properly"""
        
    #     self.assertEqual('LarryJackson278@yahoo.com', self.user.emaiL)
    
    ######################################################TESTING MELON CATEGORY TABLE####################################################################
    # def test_melon_category_creation(self):
    #     """Test melon category table and to make sure melon object has been created successfully"""
        
    #     self.assertIsInstance(self.melon_category, MelonCategory)
        
    # def test_melon_name(self):
    #     """Testing that the melon category object 'name' has been constructed properly"""
        
    #     self.assertEqual('Royal Golden Watermelon', self.melon_category.name)
    #########################################################TESTING MELON LISTING TABLE####################################################################
     def test_melon_listing_creation(self):
            """Test melon listing table and to make sure melon listing object has been created successfully"""
        
        self.assertIsInstance(self.melon_listing, MelonListing)
        
    def test_melon_description(self):
        """Testing that the melon listing object 'description' has been constructed properly"""
        
        self.assertEqual('', self.melon_listing.description)

    ################################################################TESTING BID TABLE####################################################################
    # def test_bid_creation(self):
    #     """Test bid table and to make sure bid object has been created successfully"""
        
    #     self.assertIsInstance(self.bid, Bid)
        
    # def test_bid_amount(self):
    #     """Testing that the bid object 'bid amount' has been constructed properly"""
        
    #     self.assertEqual('9.50', self.bid.bid_amount)






if __name__ == "__main__":
    
    connect_to_db(app)
    
    import unittest

    unittest.main()