import time
import math
from selenium import webdriver
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(scope='function')
def browser():
    print("\n Start browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print('\n Quit browser...')
    browser.quit()


class TestMain1:

    otvet = ""

    @pytest.mark.parametrize('links', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
    def test_find_answer(self, browser, links):
        link = f"https://stepik.org/lesson/{links}/step/1"
        browser.get(link)
        answer = str(math.log(int(time.time())))
        browser.implicitly_wait(10)
        input1 = browser.find_element_by_tag_name('textarea')
        # input1 = browser.find_element_by_css_selector("#ember93>textarea")
        input1.send_keys(answer)
        submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission')))
        # submit = browser.find_element_by_css_selector('.submit-submission')
        submit.click()
        answer_or_not_answer = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
        # answer_or_not_answer = browser.find_element_by_css_selector('.smart-hints__hint').text
        if answer_or_not_answer != "Correct!":
            self.otvet += answer_or_not_answer
        print(self.otvet)
        assert answer_or_not_answer == "Correct!", 'текст должен совпадать с "Correct!"'








