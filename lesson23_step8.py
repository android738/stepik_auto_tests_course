from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 15)
    browser.get(link)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))      

    firstBtn = browser.find_element(By.CSS_SELECTOR, "#book")
    firstBtn.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input_value"))) 

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "#solve")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()