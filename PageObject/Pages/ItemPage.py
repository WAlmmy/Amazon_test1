from selenium.common.exceptions import NoSuchElementException
from PageObject.Locators import Locator
from .BasePage import BasePage

class ItemPage(BasePage):
    def __init__(self, context, item_list):
        self.item_list=item_list
        self.add_to_cart_button=Locator.add_to_cart_button
        BasePage.__init__(self, context.driver, base_url=self.get_item_url())
        self.context=context
    
    def get_item_url(self):
        return self.item_list[0]

    def add_item_to_cart(self):
        btn=self.find_byXpath(self.add_to_cart_button)
        btn.click()

    def change_item_quantity(self, amount):
        pass