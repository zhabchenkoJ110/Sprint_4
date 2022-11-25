import allure
from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage


class TestOrderPage:

    @allure.description('Флоу позитивного сценария заказа Самоката при клике на кнопку "Заказать" вверху страницы')
    @allure.title('Первый сценарий заказа самоката по клику "Заказать" вверху страницы')
    def test_first_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_first_order_button()
        order_page = OrderPage(driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_black_checkbox()
        order_page.set_comment()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')


    @allure.description('Флоу позитивного сценария заказа Самоката при клике на кнопку "Заказать" внизу страницы')
    @allure.title('Второй сценарий заказа самоката по клику "Заказать" внизу')
    def test_second_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        main_page.click_second_order_button()
        order_page = OrderPage(driver)
        order_page.set_name()
        order_page.set_surname()
        order_page.set_address()
        order_page.set_metro_station()
        order_page.set_phone_number()
        order_page.click_next_button()

        order_page.set_date()
        order_page.set_rental_period()
        order_page.click_grey_checkbox()
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.order_has_been_placed_text().startswith('Заказ оформлен')
