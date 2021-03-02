import unittest
from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        
        browser.get("http://suninjuly.github.io/registration1.html")
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first") 
        input1.send_keys("Andrei")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Chernetsky")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Aftar.xe@gmail.com")
    
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        time.sleep(1)
    
        welcome_text_elm = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elm.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "not equal")

    def test_reg2(self):
        self.browser = webdriver.Chrome()
        browser = self.browser
        
        browser.get("http://suninjuly.github.io/registration2.html")
        input1 = browser.find_element_by_css_selector(".first_block .form-control.first") 
        input1.send_keys("Andrei")
        input2 = browser.find_element_by_css_selector(".first_block .form-control.second")
        input2.send_keys("Chernetsky")
        input3 = browser.find_element_by_css_selector(".first_block .form-control.third")
        input3.send_keys("Aftar.xe@gmail.com")
    
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
    
        time.sleep(1)
    
        welcome_text_elm = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elm.text
        
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "not equal")
        

if __name__ == "__main__":
    unittest.main()

