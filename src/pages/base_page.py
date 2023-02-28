import pytest
from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        self.driver = pytest.driver if pytest.driver is not None else webdriver.Remote()
        self.wait = int(pytest.config.getoption("--EXPLICIT_WAIT"))

    def get_title(self):
        return self.driver.title

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def wait_for_visibility(self, *locator):
        return self.get_fluent_wait().until(EC.visibility_of_element_located(*locator))

    def wait_for_invisibility(self, *locator):
        return self.get_fluent_wait().until(EC.invisibility_of_element_located(*locator))

    def wait_for_clickable(self, *locator):
        return self.get_fluent_wait().until(EC.element_to_be_clickable(*locator))

    def wait_for_alert(self):
        return self.get_fluent_wait().until(EC.alert_is_present())

    def get_fluent_wait(self):
        return WebDriverWait(self.driver, self.wait, 1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
