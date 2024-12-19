import time

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


    def test_ElementNotInteractableException(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Click Add button
        add_button_locator = driver.find_element(By.ID, 'add_btn')
        add_button_locator.click()

        #Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row2_input_locator = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        #Type text into the second input field
        row2_input_locator.send_keys("Input text")

        #Push Save button using locator By.name(“Save”)
        driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']").click()

        #Verify text saved
        confirmation_locator = wait.until(ec.presence_of_element_located((By.ID, "confirmation")))
        confirmation_text = confirmation_locator.text
        assert confirmation_text == "Row 2 was saved", "Wrong confirmation message"