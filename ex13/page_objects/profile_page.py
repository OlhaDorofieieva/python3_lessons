from selenium.webdriver.common.by import By
from ..page_objects.base_page import BasePage
from ..page_objects.locators.login_page import Locators

class ProfilePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def find_exit_href(self):
        self._element_is_visible(locator=(By.XPATH, self.locators.href_exit_xpath_locator))