import time

from pages.drag_and_drop_page import DragAndDrop


def test_drag_drop(driver):
    drag_and_drop = DragAndDrop(driver)
    drag_and_drop.open()
    drag_and_drop.draggable_1()
    drag_and_drop.draggable_2()