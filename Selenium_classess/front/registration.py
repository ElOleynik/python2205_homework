from Selenium_classess.constants.test_user_credentials import TEST_USER_LOGIN, TEST_USER_PASSWORD, \
    TEST_USER_NAME, TEST_USER_LAST_NAME
from .base import Base


class Registration(Base):
    def __init__(self):
        super().__init__()

    def fill_all_fields_on_registration_form_with_correct_data(self,
                                                               name=TEST_USER_NAME,
                                                               last_name=TEST_USER_LAST_NAME,
                                                               email=TEST_USER_LOGIN,
                                                               password=TEST_USER_PASSWORD,
                                                               repeat_password=TEST_USER_PASSWORD,
                                                               is_click=True):
        self.fill_first_name_field_on_registration_form(name)
        self.fill_last_name_field_on_registration_form(last_name)
        self.fill_email_field_on_registration_form(email)
        self.fill_password_field_on_registration_form(password)
        self.fill_repeat_password_field_on_registration_form(repeat_password)

        if is_click:
            self.click_register_button_on_registration_form()

    def registration_full_cycle(self,
                                name=TEST_USER_NAME,
                                last_name=TEST_USER_LAST_NAME,
                                email=TEST_USER_LOGIN,
                                password=TEST_USER_PASSWORD,
                                repeat_password=TEST_USER_PASSWORD):
        self.click_sign_in_from_default_page()
        self.click_register_from_sign_in_page()
        self.fill_all_fields_on_registration_form_with_correct_data(name, last_name, email, password, repeat_password)

    def fill_first_name_field_on_registration_form(self, name):
        self.registration_page.name_field().send_keys(name)

    def fill_last_name_field_on_registration_form(self, name):
        self.registration_page.last_name_field().send_keys(name)

    def fill_email_field_on_registration_form(self, name):
        self.registration_page.email_field().send_keys(name)

    def fill_password_field_on_registration_form(self, name):
        self.registration_page.password_field().send_keys(name)

    def fill_repeat_password_field_on_registration_form(self, name):
        self.registration_page.reenter_password_field().send_keys(name)

    def click_register_button_on_registration_form(self):
        self.registration_page.register_button().click()

    def click_sign_in_from_default_page(self):
        self.navigation_bar_page.sign_in_button().click()

    def click_register_from_sign_in_page(self):
        self.sign_in_page.register_button().click()
