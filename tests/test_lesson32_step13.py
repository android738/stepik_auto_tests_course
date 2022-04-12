import unittest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get(link)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Vlad")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Kalinin")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("admin@site.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        wait = WebDriverWait(browser, 10)
        browser.get(link)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input")))

        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Vlad")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Kalinin")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("admin@site.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, ".btn")
        button.click()

        # находим элемент, содержащий текст
        welcome_text_elt = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Should be absolute value of a number")
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

if __name__ == "__main__":
    unittest.main()