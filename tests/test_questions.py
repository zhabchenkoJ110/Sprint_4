import allure
from page_objects.main_page import MainPage
from page_objects.questions_page import QuestionsPage


class TestQuestions:

    @allure.description('Когда нажимаешь на стрелочку первого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_first_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_first_question()
        assert questions_page.get_first_answer() == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.description('Когда нажимаешь на стрелочку второго вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_second_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_second_question()
        assert questions_page.get_second_answer() == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

    @allure.description('Когда нажимаешь на стрелочку третьего вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_third_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_third_question()
        assert questions_page.get_third_answer() == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'


    @allure.description('Когда нажимаешь на стрелочку четвертого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_fourth_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_fourth_question()
        assert questions_page.get_fourth_answer() == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'


    @allure.description('Когда нажимаешь на стрелочку пятого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_fifth_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_fifth_question()
        assert questions_page.get_fifth_answer() == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

    @allure.description('Когда нажимаешь на стрелочку шестого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_sixth_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_sixth_question()
        assert questions_page.get_sixth_answer() == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

    @allure.description('Когда нажимаешь на стрелочку седьмого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_seventh_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_seventh_question()
        assert questions_page.get_seventh_answer() == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

    @allure.description('Когда нажимаешь на стрелочку восьмого вопроса, открывается соответствующий текст ответа')
    @allure.title('Когда нажимаешь на стрелочку, открывается соответствующий текст')
    def test_eighth_question(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')
        main_page = MainPage(driver)
        main_page.click_close_cookie()
        questions_page = QuestionsPage(driver)
        questions_page.click_eighth_question()
        assert questions_page.get_eighth_answer() == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
