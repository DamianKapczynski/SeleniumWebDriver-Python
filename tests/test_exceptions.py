import pytest
from selenium.webdriver.common.by import By

class TestExceptionsScenarios:
    def test_NoSuchElementException(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button
        add_button_locator = driver.find_element(By.ID, 'add_btn')
        add_button_locator.click()

        #Verify Row 2 input field is displayed
        row2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row2_input_locator.is_displayed(), "Row2 is not displayed but it should be"
