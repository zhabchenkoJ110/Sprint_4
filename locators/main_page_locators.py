from selenium.webdriver.common.by import By


class MainPageLocators:

    locator_ya_logo = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']
    locator_scooter_logo = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']
    locator_order_button = [By.CLASS_NAME, 'Button_Button__ra12g']
    locator_cookie_button = [By.ID, 'rcc-confirm-button']

    locator_first_question_element = [By.ID, 'accordion__heading-0']
    locator_second_question_element = [By.ID, 'accordion__heading-1']
    locator_third_question_element = [By.ID, 'accordion__heading-2']
    locator_fourth_question_element = [By.ID, 'accordion__heading-3']
    locator_fifth_question_element = [By.ID, 'accordion__heading-4']
    locator_sixth_question_element = [By.ID, 'accordion__heading-5']
    locator_seventh_question_element = [By.ID, 'accordion__heading-6']
    locator_eighth_question_element = [By.ID, 'accordion__heading-7']

    locator_first_answer_element = [[By.ID, 'accordion__panel-0']]
    locator_second_answer_element = [By.ID, 'accordion__panel-1']
    locator_third_answer_element = [By.ID, 'accordion__panel-2']
    locator_fourth_answer_element = [By.ID, 'accordion__panel-3']
    locator_fifth_answer_element = [By.ID, 'accordion__panel-4']
    locator_sixth_answer_element = [By.ID, 'accordion__panel-5']
    locator_seventh_answer_element = [By.ID, 'accordion__panel-6']
    locator_eighth_answer_element = [By.ID, 'accordion__panel-7']
