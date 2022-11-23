import allure
from page_objects.main_page import MainPage


class TestMainPage:

    @allure.description('При нажатии на логотип «Яндекс» в новом окне откроется главная страница Яндекса')
    @allure.title('Если нажать на логотип «Яндекс», в новом окне откроется главная страница Яндекса.')
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/")
        main_page.click_yandex_logo()
        assert len(driver.window_handles) == 2

    @allure.description('При нажатии на логотип «Самоката» попадёшь на главную страницу «Самоката»')
    @allure.title('Если нажать на логотип «Яндекс», то попадёшь на главную страницу «Самоката»')
    def test_click_samokat_logo(self, driver):
        main_page = MainPage(driver)
        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.click_scooter_logo()
        assert driver.current_url == "https://qa-scooter.praktikum-services.ru/"
