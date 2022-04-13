from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get(link)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".custom-select")))

    a = int(browser.find_element(By.CSS_SELECTOR, "#num1").text)
    b = int(browser.find_element(By.CSS_SELECTOR, "#num2").text)
    c = str(a+b)
    select = Select(browser.find_element(By.CSS_SELECTOR, ".custom-select"))
    select.select_by_value(c)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()