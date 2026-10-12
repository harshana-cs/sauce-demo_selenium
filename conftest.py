# this file is for defining the fixtures that can be used across the test cases. Fixtures are used to set up preconditions for tests, such as initializing a web driver, setting up a database connection, or creating test data. They help to reduce code duplication and improve test maintainability.
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver=webdriver.Edge()
    driver.maximize_window()
    #generate and injects the driver means it calls the driver function and provides the driver instance to the test functions that require it. 
   #if not used the driver gets quit 
    yield driver
    driver.quit()