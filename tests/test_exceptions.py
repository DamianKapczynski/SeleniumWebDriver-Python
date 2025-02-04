from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.exceptions_page import ExceptionsPage

class TestExceptionsScenarios:
    def test_NoSuchElementException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row_2_displayed(), "Row2 is not displayed but it should be"


    def test_ElementNotInteractableException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_text_to_2_row()
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Wrong confirmation message"


    def test_InvalidElementStateException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.clear_text_1_row()
        exception_page.add_text_to_1_row()
        assert exception_page.get_confirmation_message() == "Row 1 was saved", "Wrong confirmation message"


    def test_StaleElementReferenceException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.execute_add_button()
        assert not exception_page.are_instructions_displayed(), "Instruction text element is displayed but it shouldn't"


    def test_TimeoutException(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row_2_displayed(), "Row2 is not displayed but it should be"
