from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import logging

class Inventorypage:
    def __init__(self, driver):
        self.driver = driver
        # locators for the inventory page
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.add_button = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_button = (By.ID, "remove-sauce-labs-backpack")

    def sort_by(self, value):
        Select(self.driver.find_element(*self.sort_dropdown)).select_by_value(value)
        time.sleep(2)

    def add_to_cart(self):
        self.driver.find_element(*self.add_button).click()
        logging.info("Item added to cart")
        time.sleep(2)

    def remove_from_cart(self):
        self.driver.find_element(*self.remove_button).click()
        logging.info("Item removed from cart")
        time.sleep(2)


        #logging.warning("This is a warning message") - This gives error message in the log file. 