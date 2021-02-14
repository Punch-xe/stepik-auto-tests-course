from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
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
    
    
    
    assert "Congratulations! You have successfully registered!" == welcome_text
    
finally:
    time.sleep(10)
    browser.quit()