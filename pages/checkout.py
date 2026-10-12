from selenium.webdriver.common.by import By
import time
import logging


class Checkoutpage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_item_names = (By.CLASS_NAME, "inventory_item_name")
        self.checkout_button = (By.ID, "checkout")
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")
        self.total_label = (By.CLASS_NAME, "summary_total_label")
        self.finish_button = (By.ID, "finish")
        self.complete_header = (By.CLASS_NAME, "complete-header")
        self.back_home_button = (By.ID, "back-to-products")
        self.generate_pdf_button = (By.ID, "generate-pdf-order")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo({top: document.body.scrollHeight});")
        logging.info(f"Scrolled down on {self.driver.current_url}")
        time.sleep(2)
    def add_items(self, item_names):
        for name in item_names:
            locator = (By.XPATH, f"//div[text()='{name}']/ancestor::div[@class='inventory_item']//button")
            self.driver.find_element(*locator).click()
            logging.info(f"Added to cart: {name}")
            time.sleep(1)
    def get_cart_count(self):
        return int(self.driver.find_element(*self.cart_badge).text)
    def open_cart(self):
        self.driver.find_element(*self.cart_icon).click()
        logging.info("Cart opened")
        time.sleep(2)

    def get_cart_items(self):
        items = self.driver.find_elements(*self.cart_item_names)
        return [item.text for item in items]

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        logging.info("Checkout clicked")
        time.sleep(2)
    def enter_details(self, first_name, last_name, postal_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        logging.info("Checkout details entered")
        time.sleep(1)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        logging.info("Continue clicked")
        time.sleep(2)

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
    def get_total(self):
        total = self.driver.find_element(*self.total_label).text
        logging.info(f"Order total: {total}")
        return total

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        logging.info("Order finished")
        time.sleep(2)
    def get_confirmation_message(self):
        return self.driver.find_element(*self.complete_header).text

    def back_to_home(self):
        self.driver.find_element(*self.back_home_button).click()
        time.sleep(2)
    def click_generate_pdf(self):
        self.driver.find_element(*self.generate_pdf_button).click()
        logging.info("Generate PDF clicked")
        time.sleep(2)