import time

import pytest
from appium.webdriver.common.appiumby import AppiumBy

from base.base_page import Base
from config.root_config import SCREENSHOTS_DIR


class TestSettings(object):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self, common_driver):
        base = Base(common_driver)
        base.skip_chrome_landing()

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def test_settings(self, common_driver):
        driver = common_driver
        base = Base(driver)

        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/TestSettings_test_about_Step_1.png')
        id_general_btn = (AppiumBy.XPATH, '//XCUIElementTypeCell[@name="General"]')
        _, general_btn = base.find_element(id_general_btn)
        general_btn.click()
        time.sleep(1)

        driver.get_screenshot_as_file(f'{SCREENSHOTS_DIR}/TestSettings_test_about_Step_2.png')
        id_about_btn = (AppiumBy.XPATH, '//XCUIElementTypeCell[@name="About"]')
        _, about_btn = base.find_element(id_about_btn)
        about_btn.click()
        time.sleep(1)


if __name__ == '__main__':
    pytest.main()
