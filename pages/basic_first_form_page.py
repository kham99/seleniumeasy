from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class BasicFirstForm(BasePage):
    basic_url = 'https://demo.seleniumeasy.com/basic-first-form-demo.html'

    def __init__(self, driver):
        super().__init__(driver, self.basic_url)

    def open_page(self):
        self.driver.get(self.url)

    def enter_message(self, message):
        message_field = self.driver.find_element(By.XPATH, '//input[@id="user-message"]')
        message_field.send_keys(message)

    def submit_message(self):
        submit = self.driver.find_element(By.XPATH, '//button[@onclick="showInput();"]')
        submit.click()

    def text_result(self):
        return self.driver.find_element(By.XPATH, '//span[@title="text message"]')

    def enter_a(self, num_1):
        enter_num = self.driver.find_element(By.XPATH, '//input[@id="value1"]')
        enter_num.send_keys(num_1)

    def enter_b(self, num_2):
        enter_num = self.driver.find_element(By.XPATH, '//input[@id="value2"]')
        enter_num.send_keys(num_2)

    def submit_calc(self):
        submit = self.driver.find_element(By.XPATH, '//button[@onclick="return total()"]')
        submit.click()

    def calc_result(self):
        return self.driver.find_element(By.XPATH, '//span[@id="displayvalue"]')



