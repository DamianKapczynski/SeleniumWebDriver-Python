from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage

class TestExceptionsScenarios:
    def test_NoSuchElementException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.execute_add_button()
        assert exception_page.is_second_row_displayed(), "Row2 is not displayed but it should be"


    def test_ElementNotInteractableException(self, driver):
        #Open page
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.execute_add_button()
        exception_page.type_text()
        exception_page.execute_save_button()
        assert  exception_page.validate_second_row_input()


    def test_InvalidElementStateException(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Clear input field
        driver.find_element(By.ID, 'edit_btn').click()
        input_field_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(input_field_locator))
        input_field_locator.clear()

        #Type text into the input field
        input_field_locator.send_keys("New value")
        driver.find_element(By.ID, "save_btn").click()

        #Verify text changed
        confirmation_locator = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        assert confirmation_locator.text == "Row 1 was saved", "Wrong confirmation message"


    def test_StaleElementReferenceException(self, driver):
        #Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        #Find the instructions text element
        instruction_text_locator = driver.find_element(By.ID, 'instructions')

        #Push add button
        driver.find_element(By.ID, 'add_btn').click()

        #Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located((By.ID, 'instructions'))), "Instruction text element is displayed but it shouldn't"


    def test_TimeoutException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.execute_add_button()
        assert exception_page.is_second_row_displayed(), "Row2 is not displayed but it should be"
