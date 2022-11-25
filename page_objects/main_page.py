import allure
from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажать на логотип "Яндекса"')
    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.locator_ya_logo).click()

    @allure.step('Нажать на логотип "Самоката"')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.locator_scooter_logo).click()

    @allure.step('Закрыть cookie')
    def click_close_cookie(self):
        self.driver.find_element(*MainPageLocators.locator_cookie_button).click()

    @allure.step('Нажать на кнопку Заказать вверху страницы')
    def click_first_order_button(self):
        self.driver.find_elements(*MainPageLocators.locator_order_button)[0].click()

    @allure.step('Нажать на кнопку Заказать внизу страницы')
    def click_second_order_button(self):
        self.driver.find_elements(*MainPageLocators.locator_order_button)[2].click()
