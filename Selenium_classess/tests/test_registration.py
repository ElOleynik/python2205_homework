import allure

from Selenium_classess.constants.endpoints_constants import LOGIN_USER, DELETE_USER
from Selenium_classess.constants.test_user_credentials import TEST_USER_LOGIN, TEST_USER_PASSWORD
from Selenium_classess.tests.test_base import TestBase
from Selenium_classess.constants.url_constants import DEFAULT_API_URL


@allure.feature('User registration')
@allure.story('Registration on https://qauto2.forstudy.space/api with test user')
class TestRegistration(TestBase):
    def setup_class(self):
        super().setup_class(self)
        self.user_email = TEST_USER_LOGIN
        self.user_password = TEST_USER_PASSWORD
        self.user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def test_registration_success(self):
        self.registration.registration_full_cycle()
        with allure.step("Check user success registration"):
            assert len(self.garage.get_text_from_empty_garage()) > 0

    def teardown_method(self):
        self.session.post(url=f"{DEFAULT_API_URL}{LOGIN_USER}", json=self.user_to_delete)
        self.session.delete(f"{DEFAULT_API_URL}{DELETE_USER}")





