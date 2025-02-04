from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ExceptionsPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-exceptions/'
    __add_button = (By.ID, 'add_btn')
    __edit_button = (By.ID, 'edit_btn')
    __confirmation_element = (By.ID, "confirmation")
    __instructions_element = (By.ID, 'instructions')
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='row2']/input")
    __row_1_input_text = "Input 1 text"
    __row_2_input_text = "Input 2 text"
    __row_1_save_button = (By.XPATH, "//div[@id='row1']/button[@name='Save']")
    __row_2_save_button = (By.XPATH, "//div[@id='row2']/button[@name='Save']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_add_button(self):
        super()._click(self.__add_button)

    def add_second_row(self):
        super()._click(self.__add_button)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def is_row_2_displayed(self):
        return super()._is_displayed(self.__row_2_input_element)

    def is_second_row_displayed(self):
        return super()._is_displayed(self.__row_2_input_element)

    def add_text_to_1_row(self):
        super()._type(self.__row_1_input_element, self.__row_1_input_text)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def add_text_to_2_row(self):
        super()._type(self.__row_2_input_element, self.__row_2_input_text)
        super()._click(self.__row_2_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def clear_text_1_row(self):
        super()._click(self.__edit_button)
        super()._wait_until_element_is_clickable(self.__row_1_input_element)
        super()._clear_text(self.__row_1_input_element)

    def get_confirmation_message(self):
        return super()._get_text(self.__confirmation_element)

    def are_instructions_displayed(self):
       return super()._is_displayed(self.__instructions_element)