from pages.base_page import BasePage
from selenium.webdriver.common.by import By


RADIO_BUTTON_URL = 'https://demo.seleniumeasy.com/basic-radiobutton-demo.html'


class RadioButtonLocators:
    OPTRADIO_FEMALE = (By.XPATH, '//input[@name="optradio" and @value="Female"]')
    BUTTON_CKECK = (By.XPATH, '//button[@id="buttoncheck"]')
    OPTRADIO_MALE = (By.XPATH, '//input[@name="optradio" and @value="Male"]')
    RADIO_BUTTON = (By.XPATH, '//p[@class="radiobutton"]')
    GENDER_MALE = (By.XPATH, '//input[@name="gender" and @value="Male"]')
    GENDER_FEMALE = (By.XPATH, '//input[@name="gender" and @value="Female"]')
    VALUE_0_5 = (By.XPATH, '//input[@value="0 - 5"]')
    VALUE_5_15 = (By.XPATH, '//input[@value="5 - 15"]')
    VALUE_15_50 = (By.XPATH, '//input[@value="15 - 50"]')
    BUTTON_ONCLICK = (By.XPATH, '//button[@onclick="getValues();"]')
    GROUP_RADIOBUTTON = (By.XPATH, '//p[@class="groupradiobutton"]')


class RadioButton(BasePage):
    url = RADIO_BUTTON_URL

    def __init__(self, driver):
        super().__init__(driver, self.url)
        self.locator = RadioButtonLocators()

    def open_page(self):
        self.open()

    def radio_button_female(self):
        self.find_element(self.locator.OPTRADIO_FEMALE)
        self.click(self.locator.OPTRADIO_FEMALE)
        self.find_element(self.locator.BUTTON_CKECK)
        self.click(self.locator.BUTTON_CKECK)

    def radio_button_male(self):
        self.find_element(self.locator.OPTRADIO_MALE)
        self.click(self.locator.OPTRADIO_MALE)
        self.find_element(self.locator.BUTTON_CKECK)
        self.click(self.locator.BUTTON_CKECK)

    def text_result(self):
        return self.find_element(self.locator.RADIO_BUTTON)

    def group_button_male(self):
        self.find_element(self.locator.GENDER_MALE)
        self.click(self.locator.GENDER_MALE)

    def group_button_female(self):
        self.find_element(self.locator.GENDER_FEMALE)
        self.click(self.locator.GENDER_FEMALE)

    def age_group_0_5(self):
        self.find_element(self.locator.VALUE_0_5)
        self.click(self.locator.VALUE_0_5)

    def age_group_5_15(self):
        self.find_element(self.locator.VALUE_5_15)
        self.click(self.locator.VALUE_5_15)

    def age_group_15_50(self):
        self.find_element(self.locator.VALUE_15_50)
        self.click(self.locator.VALUE_15_50)

    def button_group(self):
        self.find_element(self.locator.BUTTON_ONCLICK)
        self.click(self.locator.BUTTON_ONCLICK)

    def group_radio_result(self):
        return self.find_element(self.locator.GROUP_RADIOBUTTON)
