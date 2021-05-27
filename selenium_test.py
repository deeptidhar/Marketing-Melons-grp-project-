import os
import unittest  
import time 
import crud
import json
from seed import create_example_data
from server import app
from model import db, connect_to_db
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")   

class TestBidMelon(unittest.TestCase):
    
    def setUp(self):
        """Stuff to do before every test."""

         
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///test_db")

        # Create tables and add sample data
        db.drop_all()
        db.create_all()
        create_example_data()
        crud.create_user('qwilliams@yahoo.com', '12345678', 'Quanisha Williams')

        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), 
                                        options=chrome_options)

    def tearDown(self):
        """Do at end of every test."""

        self.browser.quit()
        db.session.remove()
        db.drop_all()
        db.engine.dispose()
        

    def login():
        """Function to log in test user."""

        self.browser.get('http://localhost:5000/login')
        time.sleep(10)

        email = self.browser.find_element_by_id('email')
        email.send_keys("qwilliams@yahoo.com")
        password = self.browser.find_element_by_id('password')
        password.send_keys("12345678")

        btn = self.browser.find_element_by_xpath("//button[@type='submit']")

        btn.click()

        time.sleep(2)


   # This test works
    def test_title(self):
        """Testing title of browser"""

        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'BitMelon - Bid on a Melon')

    #This test works
    def test_login_pass(self):
        """Testing user login is successful"""

        self.login()

        alert = self.browser.switch_to.alert
        self.assertEqual(alert.text, "You are logged in. Go buy some melons!")
        alert.accept()    
        print(" Clicked on the OK Button in the Alert Window")
        
    
   # This test works 
    def test_login_failed(self):
        """Testing user login failed"""

        self.browser.get('http://localhost:5000/login')
        time.sleep(10)

        email = self.browser.find_element_by_id('email')
        email.send_keys("mtate@hotmail.com")
        password = self.browser.find_element_by_id('password')
        password.send_keys("mtate34")

        btn = self.browser.find_element_by_xpath("//button[@type='submit']")

        btn.click()

        time.sleep(2)

        alert = self.browser.switch_to.alert
        self.assertEqual(alert.text, "Nope. That did not work. Try again?")
        

    # def test_bid(self):
    #     """Testing for users bids"""

    #     self.login()

    #     alert = self.browser.switch_to.alert
    #     alert.accept()    
    #     print(" Clicked on the OK Button in the Alert Window")

    #     time.sleep(10)

    #     bid_btn = self.browser.find_element_by_id('2')
    #     bid_btn.click()
    #     time.sleep(2)

    #     alert = self.browser.switch_to.alert
    #     self.assertEqual(alert.text, "Enter $ amount")
    #     alert.send_keys("100")

    #     alert.accept()

    #     time.sleep(2)

    #     alert = self.browser.switch_to.alert
    #     self.assertEqual(alert.text, "Oh yeah! Juicy goodness is in your future!")
    #     alert.accept()


if __name__ == "__main__":
    

    unittest.main()