import time

import pytest

from pages.basic_first_form_page import BasicFirstForm


def test_basic_first_form(driver):
    basic_test = BasicFirstForm(driver)
    basic_test.open_page()
    input_message = 'Тестовое сообщение'
    basic_test.enter_message(input_message)
    basic_test.submit_message()
    actual_result = basic_test.text_result().text
    assert actual_result == input_message


def test_calc_basic(driver):
    calc_test = BasicFirstForm(driver)
    calc_test.open_page()
    input_a = 99
    input_b = 77
    calc_test.enter_a(input_a)
    calc_test.enter_b(input_b)
    calc_test.submit_calc()
    actual_result = int(calc_test.calc_result().text)
    expected_result = input_a + input_b
    assert actual_result == expected_result, f"Expected {expected_result}, but got {actual_result}"


