import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from locators.main_page_locators import MainPageLocators


class QuestionsPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Нажать на первый вопрос в списке")
    def click_first_question(self):
        # скролл до последнего элемента аккордиона
        last_element = self.driver.find_element(*MainPageLocators.locator_eighth_question_element)
        self.driver.execute_script("arguments[0].scrollIntoView();", last_element)
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_first_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на второй вопрос в списке")
    def click_second_question(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_second_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на третий вопрос в списке")
    def click_third_question(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_third_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на четвертый вопрос в списке")
    def click_fourth_question(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_fourth_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на пятый вопрос в списке")
    def click_fifth_question(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_fifth_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на шестой вопрос в списке")
    def click_sixth_question(self):
        element = WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_sixth_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на седьмой вопрос в списке")
    def click_seventh_question(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_seventh_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Нажать на восьмой вопрос в списке")
    def click_eighth_question(self):
        element = WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_eighth_question_element))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    @allure.step("Ответ на первый вопрос")
    def get_first_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(*MainPageLocators.locator_first_answer_element)).text

    @allure.step("Ответ на второй вопрос")
    def get_second_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_second_answer_element)).text

    @allure.step("Ответ на третий вопрос")
    def get_third_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_third_answer_element)).text

    @allure.step("Ответ на четвертый вопрос")
    def get_fourth_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_fourth_answer_element)).text

    @allure.step("Ответ на пятый вопрос")
    def get_fifth_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_fifth_answer_element)).text

    @allure.step("Ответ на шестой вопрос")
    def get_sixth_answer(self):
        return WebDriverWait(self.driver, 5).until(
            ec.visibility_of_element_located(MainPageLocators.locator_sixth_answer_element)).text

    @allure.step("Ответ на седьмой вопрос")
    def get_seventh_answer(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_seventh_answer_element)).text

    @allure.step("Ответ на восьмой вопрос")
    def get_eighth_answer(self):
        return WebDriverWait(self.driver, 10).until(
            ec.visibility_of_element_located(MainPageLocators.locator_eighth_answer_element)).text
