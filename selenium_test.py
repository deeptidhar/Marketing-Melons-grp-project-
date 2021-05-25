import os
import unittest  
import time 
import json
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")   

class TestBidMelon(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), 
                                        options=chrome_options)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:5000/')
        self.assertEqual(self.browser.title, 'BitMelon - Bid on a Melon')

    def test_login(self):
        self.browser.get('http://localhost:5000/')

        email = browser.find_element_by_id('email')
        email.send_keys("test123@test.com")
        password = browser.find_element_by_id('password')
        password.send_keys("Abc1234")

        btn = self.browser.find_element_by_xpath("//input[@type='submit']")
        btn.click()
        time.sleep(2)
        alert = self.browser.switch_to.alert
        self.assertEqual(alert.text, "Login successful")
        alert.accept()    
        print(" Clicked on the OK Button in the Alert Window")
        alert.close

