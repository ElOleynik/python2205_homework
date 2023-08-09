import json
import requests


class TestRegistration:

    def setup_class(self):
        with open("test_user.json") as f:
            user_data = json.loads(f.read())
        self.name = user_data["test_user_name"]
        self.last_name = user_data["test_user_last_name"]
        self.email = user_data["test_user_email"]
        self.password = user_data["test_user_passw"]
        self.session = requests.session()
        self.base_url = "https://qauto2.forstudy.space/api"

    def test_registration_positive(self):
        parameters = {
            "name": self.name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.password
        }

        response = self.session.post(f"{self.base_url}/auth/signup", json=parameters)
        assert response.status_code == 201
        assert response.json()["status"] == "ok"
        assert response.json()["data"] is not None

    def test_user_profile(self):
        parameters = {
            "name": self.name,
            "lastName": self.last_name,
            "email": self.email,
            "password": self.password,
            "repeatPassword": self.password
        }
        response = self.session.post(f"{self.base_url}/auth/signup", json=parameters)
        assert response.status_code == 201
        login_data = {
            "email": self.email,
            "password": self.password,
            "remember": False
        }
        login_response = self.session.post(url=f"{self.base_url}/auth/signin", json=login_data)
        assert login_response.status_code == 200
        response_profile = self.session.get(f"{self.base_url}/users/profile")
        assert response_profile.status_code == 200
        assert response_profile.json()["status"] == "ok"
        assert response_profile.json()["data"]["name"] == self.name
        assert response_profile.json()["data"]["lastName"] == self.last_name

    def teardown_method(self):
        login_data = {
            "email": self.email,
            "password": self.password,
            "remember": False
        }
        self.session.post(url=f"{self.base_url}/auth/signin", json=login_data)

        self.session.delete(url=f"{self.base_url}/users/")
