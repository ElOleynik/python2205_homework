from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistrationTest:
    def setup_class(self):
        self.base_url = "https://qauto2.forstudy.space/api"
        self.driver = webdriver.Chrome()
        self.driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
        self.driver.implicitly_wait(5)

        self.session = requests.session()
        self.user_name = "Tom"
        self.user_lastname = "Araya"
        self.user_email = "testuser@test.com"
        self.user_password = "Qwerty1234"

    def test_registration(self):
        sign_in_button = self.driver.find_element(By.XPATH, "//button[text()='Sign In']")
        sign_in_button.click()
        self.driver.find_element(By.XPATH, "//button[text()='Registration']").click()
        name_field = self.driver.find_element(By.ID, "signupName")
        last_name_field = self.driver.find_element(By.ID, "signupLastName")
        email_field = self.driver.find_element(By.ID, "signupEmail")
        password_field = self.driver.find_element(By.ID, "signupPassword")
        reenter_password_field = self.driver.find_element(By.ID, "signupRepeatPassword")

        name_field.send_keys(self.user_name)
        last_name_field.send_keys(self.user_lastname)
        email_field.send_keys(self.user_email)
        password_field.send_keys(self.user_password)
        reenter_password_field.send_keys(self.user_password)
        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()
        assert len(self.driver.find_elements(By.XPATH, "//p[text()='You don’t have any cars in your garage']")) > 0

        add_car_button = self.driver.find_element(By.XPATH, "//button[text()='Add car']")
        add_car_button.click()
        assert len(self.driver.find_elements(By.XPATH, "//h4[text()='Add a car']")) > 0
        car_brand_button = self.driver.find_element(By.ID, "addCarBrand")
        car_brand_button.click()
        select_car = Select(WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH,
                            "//select[starts-with(@id, 'addCarBrand')]"))))
        select_car.select_by_visible_text('Fiat')
        car_model_button = self.driver.find_element(By.ID, "addCarModel")
        car_model_button.click()
        select_model = Select(WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable
                              ((By.XPATH,  "//select[starts-with(@id, 'addCarModel')]"))))
        select_model.select_by_visible_text('Punto')
        mil_field = self.driver.find_element(By.ID, "addCarMileage")
        mil_field.send_keys("1")
        self.driver.find_element(By.XPATH, "//button[text()='Add']").click()
        assert len(self.driver.find_elements(By.XPATH, "//p[text()='Fiat Punto']")) > 0

        user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }
        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_to_delete)
        cars_in_garage = self.session.get(f"{self.base_url}/cars")
        assert cars_in_garage.status_code == 200
        assert cars_in_garage.json()["status"] == "ok"
        assert cars_in_garage.json()["data"][0]["brand"] == "Fiat"
        assert cars_in_garage.json()["data"][0]["model"] == "Punto"
        assert cars_in_garage.json()["data"][0]["mileage"] == 1

    def teardown_method(self):
        user_to_delete = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

        self.session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=user_to_delete)
        self.session.delete("https://qauto2.forstudy.space/api/users")
