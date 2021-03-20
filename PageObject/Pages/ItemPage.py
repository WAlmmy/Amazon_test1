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
        return self.item_list[0]

    def add_item_to_cart(self):
        btn=self.find_byXpath(self.add_to_cart_button)
        btn.click()

    def change_item_quantity(self, amount):
        #self.find_byXpath(item_quantity)
        quantity_select=self._get_quantity_select()
        print(quantity_select)
        quantity_select.select_by_value(str(amount))
        print("changed quantity")
    
    def get_max_quantity(self):
        print("getting max quantity...")
        quantity_select=self._get_quantity_select()
        print(quantity_select)
        
        max_quantity=len(quantity_select.options)
        print("found max quantity...")
        return max_quantity
    
    def _get_quantity_select(self):
        return Select(self.find_byXpath(self.item_quantity))