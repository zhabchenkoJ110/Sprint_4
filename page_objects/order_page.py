import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPageLocators


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Введите имя')
    def set_name(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[0].send_keys('Тест')

    @allure.step('Введите фамилию')
    def set_surname(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[1].send_keys('Тестов')

    @allure.step('Введите адрес')
    def set_address(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[2].send_keys('Москва, Ленинский проспект, 33')

    @allure.step('Введите станцию метро')
    def set_metro_station(self):
        self.driver.find_element(*OrderPageLocators.metro_station_input).send_keys('Ленинский проспект')
        self.driver.find_element(*OrderPageLocators.metro_station_row).click()

    @allure.step('Введите номер телефона')
    def set_phone_number(self):
        self.driver.find_elements(*OrderPageLocators.inputs)[3].send_keys('+79111351234')

    @allure.step('Нажать кнопку Далее')
    def click_next_button(self):
        self.driver.find_element(*OrderPageLocators.next_button).click()

    @allure.step('Введите дату')
    def set_date(self):
        self.driver.find_elements(*OrderPageLocators.inputs_second_page)[0].send_keys('03.12.2022')
        self.driver.find_element(*OrderPageLocators.date_picker_selected).click()

    @allure.step('Выберите срок аренды')
    def set_rental_period(self):
        self.driver.find_element(*OrderPageLocators.dropdown_control).click()
        self.driver.find_elements(*OrderPageLocators.dropdown_option)[0].click()  # сутки

    @allure.step('Кликнуть черный чек-бокс')
    def click_black_checkbox(self):
        self.driver.find_element(*OrderPageLocators.black_checkbox).click()

    @allure.step('Кликнуть серый чек-бокс')
    def click_grey_checkbox(self):
        self.driver.find_element(*OrderPageLocators.grey_checkbox).click()

    @allure.step('Написать комментарий')
    def set_comment(self):
        self.driver.find_elements(*OrderPageLocators.inputs_second_page)[1].send_keys('Заказать самокат')

    @allure.step('Нажать кнопку Заказать')
    def click_order_button(self):
        self.driver.find_element(*OrderPageLocators.order_button).click()

    @allure.step('Нажать кнопку Да')
    def click_yes_button(self):
        self.driver.find_element(*OrderPageLocators.yes_button).click()

    @allure.step('Получить текст "Заказ оформлен"')
    def order_has_been_placed_text(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(OrderPageLocators.order_has_been_placed)).text
