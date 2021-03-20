from selenium.common.exceptions import NoSuchElementException
from .BasePage import BasePage

class HomePage(BasePage):
    def __init__(self, context):
        BasePage.__init__(self, context.driver)

    def get_coart_count(self):
        print(self.cart_count_span)
        return 
