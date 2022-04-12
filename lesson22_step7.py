from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os 

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get(link)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#file")))

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')       

    firstname = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    firstname.send_keys("Vladislav")
    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys("Kalinin")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("admin@site.com")
    file = browser.find_element(By.CSS_SELECTOR, "#file")
    file.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()