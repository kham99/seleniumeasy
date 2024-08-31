from pages.base_page import BasePage
from selenium.webdriver.common import By


BASIC_FIRST_FORM_URL = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'


class BasicFirstFormLocators:
    USER_MESSAGE = (By.XPATH, '//input[@id="user-message"]')
    BUTTON_ONCLICK = (By.XPATH, '//button[@onclick="showInput();"]')
    TITLE_TEXT_MESSAGE = (By.XPATH, '//span[@title="text message"]')
    INPUT_1 = (By.XPATH, '//input[@id="value1"]')
    INPUT_2 = (By.XPATH, '//input[@id="value2"]')
    BUTTON_RETURN_TOTAL = (By.XPATH, '//button[@onclick="return total()"]')
    DISPLAY_VALUE = (By.XPATH, '//span[@id="displayvalue"]')


class BasicFirstForm(BasePage):

    url = BASIC_FIRST_FORM_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)
        self.locators = BasicFirstFormLocators()

    def open_page(self):
        self.open()

    def enter_message(self, message):
        message_field = self.find_element(self.locators.USER_MESSAGE)
        message_field.send_keys(message)

    def submit_message(self):
        self.find_element(self.locators.BUTTON_ONCLICK)
        self.click(self.locators.BUTTON_ONCLICK)

    def text_result(self):
        return self.find_element(self.locators.TITLE_TEXT_MESSAGE)

    def enter_a(self, num_1):
        enter_num = self.find_element(self.locators.INPUT_1)
        enter_num.send_keys(num_1)

    def enter_b(self, num_2):
        enter_num = self.find_element(self.locators.INPUT_2)
        enter_num.send_keys(num_2)

    def submit_calc(self):
        self.find_element(self.locators.BUTTON_RETURN_TOTAL)
        self.click(self.locators.BUTTON_RETURN_TOTAL)

    def calc_result(self):
        return self.find_element(self.locators.DISPLAY_VALUE)