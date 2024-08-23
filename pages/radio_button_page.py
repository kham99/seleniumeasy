from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RadioButton(BasePage):
    radio_button_url = 'https://demo.seleniumeasy.com/basic-radiobutton-demo.html'

    def __init__(self, driver):
        super().__init__(driver, self.radio_button_url)

    def open_page(self):
        self.driver.get(self.url)

    def radio_button_female(self):
        female = self.driver.find_element(By.XPATH, '//input[@name="optradio" and @value="Female"]')
        female.click()
        button = self.driver.find_element(By.XPATH, '//button[@id="buttoncheck"]')
        button.click()

    def radio_button_male(self):
        male = self.driver.find_element(By.XPATH, '//input[@name="optradio" and @value="Male"]')
        male.click()
        button = self.driver.find_element(By.XPATH, '//button[@id="buttoncheck"]')
        button.click()

    def text_result(self):
        return self.driver.find_element(By.XPATH, '//p[@class="radiobutton"]')

    def group_button_male(self):
        male = self.driver.find_element(By.XPATH, '//input[@name="gender" and @value="Male"]')
        male.click()

    def group_button_female(self):
        female = self.driver.find_element(By.XPATH, '//input[@name="gender" and @value="Female"]')
        female.click()

    def age_group_0_5(self):
        group = self.driver.find_element(By.XPATH, '//input[@value="0 - 5"]')
        group.click()

    def age_group_5_15(self):
        group = self.driver.find_element(By.XPATH, '//input[@value="5 - 15"]')
        group.click()

    def age_group_15_50(self):
        group = self.driver.find_element(By.XPATH, '//input[@value="15 - 50"]')
        group.click()

    def button_group(self):
        button = self.driver.find_element(By.XPATH, '//button[@onclick="getValues();"]')
        button.click()

    def group_radio_result(self):
        return self.driver.find_element(By.XPATH, '//p[@class="groupradiobutton"]')



