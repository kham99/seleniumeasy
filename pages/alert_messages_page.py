from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AlertMessages(BasePage):
    url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open(self):
        self.driver.get(self.url)

    def autocloseable_success(self):
        button = self.driver.find_element(By.XPATH, '//button[@id = "autoclosable-btn-success"]')
        button.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH,
            '//div[@class = "alert alert-success alert-autocloseable-success"]')))
        wait.until(EC.invisibility_of_element_located((By.XPATH,
            '//div[@class = "alert alert-success alert-autocloseable-success"]')))

    def normal_success(self):
        button = self.driver.find_element(By.XPATH, '//button[@id = "normal-btn-success"]')
        button.click()
        wait = WebDriverWait(self.driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class = "alert alert-success alert-normal-success"]')))
        close = self.driver.find_elements(By.XPATH, '//button[@class="close"]')
        close[0].click()
        wait.until(EC.invisibility_of_element_located(
            (By.XPATH, '//div[@class = "alert alert-success alert-normal-success"]')))
