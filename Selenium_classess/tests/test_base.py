import requests

from Selenium_classess.driver.custom_driver import Driver
from Selenium_classess.front.garage import Garage
from Selenium_classess.front.registration import Registration
from Selenium_classess.constants.url_constants import DEFAULT_URL


class TestBase:

    def setup_class(self):
        self.driver = Driver().driver
        self.driver.get(DEFAULT_URL)
        self.registration = Registration()
        self.garage = Garage()
        self.session = requests.session()
