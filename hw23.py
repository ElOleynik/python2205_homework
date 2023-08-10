from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCoreShop:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://coremetalshop.com.ua/")
        self.driver.implicitly_wait(5)

    def test_find_locators(self):
        self.driver.find_element(By.XPATH, "//*[@id='logo']/center/a/img")
        self.driver.find_element(By.XPATH, "//a[text()='Одяг']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Дитячі футболки']").click()
        self.driver.find_element(By.XPATH, "//input[@value=44]").click()
        self.driver.find_element(By.ID, "button-filter").click()
        self.driver.find_element(By.XPATH, "//a[text()='Детская Футболка Metallica']").click()
        assert len(self.driver.find_elements(By.XPATH, "//h3[text()='Доступні опції']")) > 0
        self.driver.find_element(By.ID, "input-option972").click()
        self.driver.find_element(By.XPATH, "//option[@value='3734']").click()
        quantity = self.driver.find_element(By.ID, "input-quantity")
        quantity.clear()
        quantity.send_keys("2")
        self.driver.find_element(By.ID, "button-cart").click()
        assert len(self.driver.find_elements(By.XPATH, "//div[@class='alert alert-success']")) > 0
        self.driver.find_element(By.XPATH, "//span[@id='cart-total']").click()
        self.driver.find_element(By.XPATH, "//strong[text()=' Перейти в кошик']").click()
        assert len(self.driver.find_elements(By.XPATH, "//a[text()='Кошик замовлень']")) > 0
        buy_quantity = self.driver.find_element(By.XPATH, "//*[@id='content']/form/div/table/tbody/tr/td[4]/div/input")
        buy_quantity.clear()
        buy_quantity.send_keys("1")
        self.driver.find_element(By.XPATH, "//i[@class='fa fa-refresh']").click()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()
        self.driver.find_element(By.XPATH, "//a[text()='Продолжить']").click()
