from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfullyPage:
    _url = "https://practicetestautomation.com/logged-in-successfully/"
    __header_locator = (By.TAG_NAME, "h1")
    __log_out_button_locator = (By.LINK_TEXT, "Log out")

    def __int__(self, driver: WebDriver):
        self._driver = driver


    @property
    def get_expected_url(self) -> str:
        return self._url

    @property
    def get_header(self) -> str:
        return self._driver.find_element(self.__header_locator).text

    def is_logout_button_displayed(self) -> bool:
        return self._driver.find_element(__log_out_button_locator).is_displayed()
