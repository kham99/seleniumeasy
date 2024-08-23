from pages.alert_messages_page import AlertMessages


def test_autocloseable_success(driver):
    auto_success = AlertMessages(driver)
    auto_success.open()
    auto_success.autocloseable_success()


def test_normal_success(driver):
    normal_success = AlertMessages(driver)
    normal_success.open()
    normal_success.normal_success()
