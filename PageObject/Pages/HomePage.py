from selenium.common.exceptions import NoSuchElementException
from PageObject.Locators import Locator
from .BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver, base_url="https://www.amazon.co.uk")
        self.context=context


