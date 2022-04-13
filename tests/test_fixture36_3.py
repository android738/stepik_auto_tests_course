import re
import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

result = []
items = ["236895","236896","236897","236898","236899","236903","236904","236905"]

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('id', items)
def test_guest_should_see_login_link(browser, id):
    wait = WebDriverWait(browser, 10)
    link = f"https://stepik.org/lesson/{id}/step/1"
    browser.get(link)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "textarea")))
    browser.find_element(By.CSS_SELECTOR, "textarea").send_keys(math.log(int(time.time())))
    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    hint_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
    if (hint_text != "Correct!"):
        result.append(hint_text)
        print(' '.join(result))
    assert hint_text == "Correct!", "Hint text is not correct!"
