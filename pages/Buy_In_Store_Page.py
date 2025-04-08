from selenium.webdriver.common.by import By
import allure

class BuyInStorePage():
    allure.step("Открытие сайта магазина")
    def __init__(self, driver):
        self._driver = driver
        self._driver.get('https://www.saucedemo.com/')
    
    allure.step("Ввод имени пользователя в поле username")

    def authorization_username(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(term)
    
    allure.step("Ввод пароля в поле password и нажатие кнопки login")

    def authorization_password(self, term):   
        self._driver.find_element(By.CSS_SELECTOR, '#password').send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    allure.step("Добавление товаров в корзину")

    def add_to_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self._driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
    
     
    allure.step("Переход в корзину")


    def shopping_cart(self):
        self._driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link').click()
    
    allure.step("Переход к оформлению")

    def checkout(self):
        self._driver.find_element(By.CSS_SELECTOR, '#checkout').click()
    

    allure.step("Ввод имени в поле First Name")

    def input_first_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(term)

    allure.step("Ввод фамилии в поле Last Name")

    def input_last_name(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(term)
    
    allure.step("Ввод индекса в поле ZIP/Postal Code")

    def input_postal_code(self, term):
        self._driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(term)
    
    allure.step("Нажатие кнопки Continue")

    def button_continue(self):
        self._driver.find_element(By.CSS_SELECTOR, '#continue').click()
    
    allure.step("Отображение итоговой стоимости")

    def summary_total(self):
        total = self._driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return total
