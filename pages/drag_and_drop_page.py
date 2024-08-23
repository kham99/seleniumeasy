from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class DragAndDrop(BasePage):
    url = 'https://demo.seleniumeasy.com/drag-and-drop-demo.html'

    def __init__(self, driver):
        super().__init__(driver, self.url)

    def open(self):
        self.driver.get(self.url)

    def draggable_1(self):
        draggables = self.driver.find_elements(By.XPATH, '//span[@draggable ="true"]')
        draggable1 = draggables[0]
        target = self.driver.find_element(By.ID, 'mydropzone')
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable1, target).perform()

    def draggable_2(self):
        draggables = self.driver.find_elements(By.XPATH, '//span[@draggable ="true"]')
        draggable2 = draggables[1]
        target = self.driver.find_element(By.ID, 'mydropzone')
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable2, target).perform()

