from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.BuyOnStorePage import BuyOnStorePage
import allure

@allure.title("Заказ в интернет-магазине ")
@allure.description("Добавление в корзину товаров: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie")
@allure.feature("FUNCTIONALITY")
@allure.severity("critical")

def test_buy_on_store():
    with allure.step("Открытие браузера"):
     browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
     
    with allure.step("Открытие страницы сайта"):
      buy = BuyOnStorePage(browser)   
    
    with allure.step("Ввод в поле username"):
      buy.authorization_username('standard_user')
    
    with allure.step("Ввод в поле password"):
       buy.authorization_password('secret_sauce')
    
    with allure.step("Добавление в корзину товаров"):
      buy.add_to_cart()
    
    with allure.step("Переход в корзину"):
      buy.shopping_cart()
    
    with allure.step("Переход к оформлению"):
      buy.checkout()

    with allure.step("Ввод имени получателя в поле First Name"):
      buy.input_first_name('Ksenia')

    with allure.step("Вводи фамилии получателя в поле Last Name"):
      buy.input_last_name('Rayevskaya')

    with allure.step("Ввод индекса в поле Zip/Postal Code"):
     buy.input_postal_code('12345')

    with allure.step("Нажатие кнопки Continue"):
     buy.button_continue()
     
    with allure.step("Отображение итоговой стоимости"):
     total = buy.summary_total()

    with allure.step("Проверка итоговой стоимости"):
      assert total == 'Total: $58.29'

    browser.quit()