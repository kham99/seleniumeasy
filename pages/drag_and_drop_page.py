from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


DRAG_AND_DROP_URL = 'https://demo.seleniumeasy.com/drag-and-drop-demo.html'


class DragAndDropLocators:
    DRAGGABLE = (By.XPATH, '//span[@draggable ="true"]')
    MYDROPZONE = (By.ID, 'mydropzone')


class DragAndDrop(BasePage):
    url = DRAG_AND_DROP_URL

    def __init__(self, driver):
        self.locator = DragAndDropLocators()
        super().__init__(driver, self.url)

    def open(self):
        self.open()

    def draggable_1(self):
        draggables = self.find_element(self.locator.DRAGGABLE)
        draggable1 = draggables[0]
        target = self.find_element(self.locator.MYDROPZONE)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable1, target).perform()

    def draggable_2(self):
        draggables = self.find_element(self.locator.DRAGGABLE)
        draggable2 = draggables[1]
        target = self.find_element(self.locator.MYDROPZONE)
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(draggable2, target).perform()
