import pytest
from selenium import webdriver
from pages.inventory import Inventorypage
from pages.login import Loginpage


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_inventory(driver):
    login_obj = Loginpage(driver)
    login_obj.open_url("https://www.saucedemo.com/")
    login_obj.enter_username("standard_user")
    login_obj.enter_password("secret_sauce")
    login_obj.click_login()
    obj = Inventorypage(driver)
    obj.sort_by("hilo")
    obj.add_to_cart()
    obj.remove_from_cart()

# from pages.login import Loginpage
# from pages.inventory import Inventorypage


# def test_inventory(driver):          # driver comes from conftest.py automatically
#     login_obj = Loginpage(driver)
#     login_obj.open_url("https://www.saucedemo.com/")
#     login_obj.enter_username("standard_user")
#     login_obj.enter_password("secret_sauce")
#     login_obj.click_login()
#     assert "inventory.html" in driver.current_url, "Login failed"

#     obj = Inventorypage(driver)

#     obj.sort_by("hilo")
#     prices = obj.get_prices()
#     assert prices == sorted(prices, reverse=True), f"Not sorted high to low: {prices}"

#     obj.add_to_cart()
#     assert obj.get_cart_count() == 1, "Cart badge should show 1"

#     obj.remove_from_cart()
#     assert obj.get_cart_count() == 0, "Cart should be empty after removing"