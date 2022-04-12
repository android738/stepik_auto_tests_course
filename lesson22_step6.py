from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 10)
    browser.get(link)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input_value")))

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    checkBox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    checkBox.click()

    radioButton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    browser.execute_script("return arguments[0].click();", radioButton)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script("return arguments[0].click();", submit)

finally:
    time.sleep(10)
    browser.quit()