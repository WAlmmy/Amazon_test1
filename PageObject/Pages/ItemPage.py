from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from PageObject.Locators import Locator
from .BasePage import BasePage

class ItemPage(BasePage):
    def __init__(self, context, item_list):
        self.item_list=item_list
        self.add_to_cart_button=Locator.add_to_cart_button
        self.item_quantity=Locator.item_quantity
        BasePage.__init__(self, context.driver, base_url=self.get_item_url())
        self.context=context
    
    def get_item_url(self):
        item_url=self.item_list[0]
        return item_url

    def get_item_href(self):
        item_href=self.item_list[1]
        return item_href

    def add_item_to_cart(self):
        btn=self.find_byXpath(self.add_to_cart_button)
        btn.click()

    def change_item_quantity(self, amount):
        quantity_select=self._get_quantity_select()
        quantity_select.select_by_value(str(amount))
    
    def get_max_quantity(self):
        quantity_select=self._get_quantity_select()
        max_quantity=len(quantity_select.options)
        return max_quantity
    
    def _get_quantity_select(self):
        return Select(self.find_byXpath(self.item_quantity))