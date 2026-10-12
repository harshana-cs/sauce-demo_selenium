import pytest
from selenium import webdriver
from pages.login import Loginpage
from pages.checkout import Checkoutpage


ITEMS = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
]


@pytest.fixture()
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def login(driver):
    login_obj = Loginpage(driver)
    login_obj.open_url("https://www.saucedemo.com/")
    login_obj.enter_username("standard_user")
    login_obj.enter_password("secret_sauce")
    login_obj.click_login()


def test_checkout(driver):
    login(driver)
    checkout = Checkoutpage(driver)
    checkout.add_items(ITEMS)
    checkout.scroll_down()
    assert checkout.get_cart_count() == len(ITEMS)
    checkout.open_cart()
    assert sorted(checkout.get_cart_items()) == sorted(ITEMS)
    checkout.scroll_down()
    checkout.click_checkout()
    checkout.enter_details("John", "Doe", "5000")
    checkout.click_continue()
    checkout.scroll_down()
    assert "Total" in checkout.get_total()
    checkout.click_finish()
    assert checkout.get_confirmation_message() == "Thank you for your order!"
    # checkout.back_to_home()
    checkout.click_generate_pdf()


# def test_checkout_without_postal_code(driver):
#     login(driver)
#     checkout = Checkoutpage(driver)

#     checkout.add_items(ITEMS)
#     checkout.scroll_down()
#     checkout.open_cart()

#     checkout.scroll_down()
#     checkout.click_checkout()

#     checkout.enter_details("John", "Doe", "")   
#     checkout.click_continue()

#     assert checkout.get_error_message() == "Error: Postal Code is required"