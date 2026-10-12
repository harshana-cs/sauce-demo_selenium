from selenium import webdriver
import pytest
from pages.login import Loginpage


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


# parametrize goes directly above the TEST function
@pytest.mark.parametrize("username, password, should_pass", [
    ("standard_user",           "secret_sauce", True),
    ("locked_out_user",         "secret_sauce", False),
    ("problem_user",            "secret_sauce", True),
    ("performance_glitch_user", "secret_sauce", True),
])
def test_login(driver, username, password, should_pass):
    obj = Loginpage(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username(username)
    obj.enter_password(password)
    obj.click_login()
    if should_pass:
        assert "inventory" in driver.current_url, \
            f"Login failed for user: {username}"
    else:
        assert "inventory" not in driver.current_url, \
            f"Locked-out user should not be able to log in: {username}"
# def test_invalid_login(driver):
#     obj = Loginpage(driver)
#     obj.open_url("https://www.saucedemo.com/")
#     obj.enter_username("wrong_user")
#     obj.enter_password("wrong_pass")
#     obj.click_login()
#     assert "inventory.html" not in driver.current_url
