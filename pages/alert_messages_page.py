from selenium.webdriver.common import By
from pages.base_page import BasePage


ALLERT_MESSAGE_URL = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'


class AlertMessagesLocators:
    AUTOCLOSEABLE_BTN = (By.XPATH, '//button[@id = "autoclosable-btn-success"]')
    AUTOCLOSEABLE_ALERT = (By.XPATH, '//div[@class = "alert alert-success alert-autocloseable-success"]')
    NORMAL_BTN_SUCCESS = (By.XPATH, '//button[@id = "normal-btn-success"]')
    NORMAL_ALERT_SUCCESS = (By.XPATH, '//div[@class = "alert alert-success alert-normal-success"]')
    NORMAL_SUCCESS_BUTTON_CLOSE = (By.XPATH, '//button[@class="close"]')


class AlertMessages(BasePage):
    url = ALLERT_MESSAGE_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)
        self.locators = AlertMessagesLocators()

    def open(self):
        self.open()

    def autocloseable_success(self):
        self.click(self.locators.AUTOCLOSEABLE_BTN)
        self.wait_visible_element(self.locators.AUTOCLOSEABLE_ALERT)
        self.wait_invisible_element(self.locators.AUTOCLOSEABLE_ALERT)

    def normal_success(self):
        self.find_element(self.locators.AUTOCLOSEABLE_BTN)
        self.click(self.locators.AUTOCLOSEABLE_BTN)
        self.wait_visible_element(self.locators.NORMAL_ALERT_SUCCESS)
        self.find_element(self.locators.NORMAL_SUCCESS_BUTTON_CLOSE)
        self.click(self.locators.NORMAL_SUCCESS_BUTTON_CLOSE)
        self.wait_invisible_element(self.locators.NORMAL_ALERT_SUCCESS)
