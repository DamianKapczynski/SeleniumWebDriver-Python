import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class TestExceptionsScenarios:
    def test_NoSuchElementException(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button
        add_button_locator = driver.find_element(By.ID, 'add_btn')
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        #Verify Row 2 input field is displayed
        assert row2_input_locator.is_displayed(), "Row2 is not displayed but it should be"
