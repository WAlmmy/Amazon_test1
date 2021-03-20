from selenium.common.exceptions import NoSuchElementException
from PageObject.Locators import Locator
from .BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver, base_url="https://www.amazon.co.uk")
        self.cart_count_span=Locator.cart_count_span
        self.context=context

    def go_to_page(self):
        print("going to: " + self.base_url)
        self.context.driver.get(self.base_url)

    def get_cart_count(self):
        cart_count=self.find_byXpath(self.cart_count_span)
        print(cart_count)
        return cart_count
