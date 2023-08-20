from Selenium_classess.pages.garage_page import GaragePage
from Selenium_classess.pages.navigation_bar_page import NavigationBarPage
from Selenium_classess.pages.registration_page import RegistrationPage
from Selenium_classess.pages.sign_in_page import SignInPage


class Base:
    def __init__(self):
        self.registration_page = RegistrationPage()
        self.navigation_bar_page = NavigationBarPage()
        self.sign_in_page = SignInPage()
        self.garage_page = GaragePage()
