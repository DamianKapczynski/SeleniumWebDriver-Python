from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class ExceptionsPage(BasePage):
    __url = 'https://practicetestautomation.com/practice-test-exceptions/'
    __add_button = (By.ID, 'add_btn')
    __second_row_input = (By.XPATH, "//div[@id='row2']/input")
    __input_to_second_row = "Input text"
    __save_button = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def execute_add_button(self):
        super()._click(self.__add_button)

    def execute_save_button(self):
        super()._click(self.__save_button)

    def is_second_row_displayed(self) -> bool:
        return super()._is_displayed(self.__second_row_input)

    def type_text(self):
        return  super()._type(self.__second_row_input, self.__input_to_second_row)

    def validate_second_row_input(self):
        return super()._get_text(self.__second_row_input) == self.__input_to_second_row, "Wrong input"