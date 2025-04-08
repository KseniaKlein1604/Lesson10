from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import allure

class CalculatorPage():
    allure.step("Открытие сайта калькулятора")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        self._driver.implicitly_wait(50)
    
    allure.step("Ввод числа в поле со временем ")
    def delay(self, term):
        delay = self._driver.find_element(By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(term)

    allure.step("Нажатие цифр на кнопке калькулятора")
    def click(self):
        self._driver.find_element(By.XPATH, "//*[contains(text(),'7')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'+')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'8')]").click()
        self._driver.find_element(By.XPATH, "//*[contains(text(),'=')]").click()

    allure.step("Ожидание результата")
    def screen(self):
        screen = self._driver.find_element(By.CSS_SELECTOR, 'div.screen')
        WebDriverWait(self._driver, 50).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
        )
        return screen.text