from selenium.webdriver.common.by import By
import time
class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username= (By.ID, "user-name")
        self.password= (By.ID, "password")
        self.login_button= (By.ID, "login-button")
    def open_url(self, url):
        self.driver.get(url)
        time.sleep(2)
        #hastricks are used for tuple unpacking, which allows you to pass the elements of a tuple as separate arguments to a function. In this case, the * operator is used to unpack the tuple containing the locator strategy and value for each element (username, password, and login_button) when calling the find_element method.
    def enter_username(self, username):
        self.driver.find_element(*self.username).send_keys(username)
        time.sleep(2)
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(2)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        time.sleep(2)