import time

import pytest
from pages.radio_button_page import RadioButton


def test_check_radio_button(driver):
    check_test = RadioButton(driver)
    check_test.open()
    check_test.radio_button_male()
    actual_result = check_test.text_result().text
    assert actual_result == "Radio button 'Male' is checked"


def test_check_group_radio_button(driver):
    check_test_group = RadioButton(driver)
    check_test_group.open()
    check_test_group.group_button_female()
    check_test_group.age_group_5_15()
    check_test_group.button_group()
    actual_result = check_test_group.group_radio_result().text
    assert actual_result == 'Sex : Female\nAge group: 5 - 15'


