from selenium.webdriver.common.by import By
from Selenium_classess.controls.controls import Controls
from .base_page import BasePage


class NavigationBarPage(BasePage):
    def __init__(self):
        super().__init__()
        self.sign_in_button = lambda: Controls(self._driver.find_element(By.XPATH, "//button[text()='Sign In']"))
