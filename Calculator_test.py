from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.CalculatorPage import CalculatorPage
import allure

@allure.title("Рассчет на калькуляторе")
@allure.description("Сложение двух чисел с результатом через 45 секунд ")
@allure.feature("FUNCTIONALITY")
@allure.severity("critical")

def test_calculator():
 with allure.step("Открытие браузера"):
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))

 with allure.step("Открытие страницы"):
    calculator = CalculatorPage(browser)

 with allure.step("Ввод в поле значение 45"):
        calculator.delay('45')

 with allure.step("Ввод чисел"):
    calculator.click()

 with allure.step("Ожидание результата через 45 секунд"):
    screen = calculator.screen()

 with allure.step("Проверка суммы"):
    assert screen == '15'

    browser.quit()