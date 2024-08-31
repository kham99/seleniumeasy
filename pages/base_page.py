from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def wait_visible_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.visibility_of_element_located(locator))

    def wait_invisible_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.invisibility_of_element_located(locator))

    def wait_clickable_element(self, locator):
        wait = WebDriverWait(self.driver, 5)
        wait.until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        self.wait_visible_element()
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find_element(locator).click()
