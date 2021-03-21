from PageObject.Locators import Locator
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from .BasePage import BasePage

class BasketPage(BasePage):

    def __init__(self, context):
        self.add_to_cart_button=Locator.add_to_cart_button
        self.basket_item_quantity=Locator.basket_item_quantity
        self.basket_item=Locator.basket_item
        BasePage.__init__(self, context.driver, base_url="https://www.amazon.co.uk/gp/cart/view.html?ref_=nav_cart")
        self.context=context

    def save_item_list(self):
        self.saved_item_list=self._get_items_in_basket()
        

    def change_item_quantity(self, amount, element=None):
        """
        changes number of items in item quantity dropdown
        """
        if element is None:
            element=self.driver
        #self.find_byXpath(item_quantity)
        quantity_select=self._get_quantity_select()
        print(quantity_select)
        if amount == 0:
            amount_str = "0 (Delete)"
        else:
            amount_str = str(amount)
        quantity_select.select_by_value(amount_str)
        print("changed quantity")
    
    def get_max_quantity(self):
        """
        Returns max quantity in item quanitity dropdown
        """
        print("getting max quantity...")
        quantity_select=self._get_quantity_select()
        print(quantity_select)
        
        max_quantity=len(quantity_select.options)-1
        print("found max quantity...")
        return max_quantity

    def get_item_quantity(self):
        """
        Returns an integer of the quantity of an item
        """
        quantity_select=self._get_quantity_select()
        selected_option = quantity_select.first_selected_option
        print("selected_option: " + str(selected_option))
        print("text: "+selected_option.text)
        print(type(selected_option.text))
        return int(selected_option.text)
    
    def _get_quantity_select(self):
        """
        returns a Select object of item quantity dropdown
        """
        return Select(self.find_byXpath(self.basket_item_quantity))

    def _get_items_in_basket(self):
        """
        returns a list of items in basket
        """
        return Select(self.find_byXpath(self.basket_item))

    def _get_item_name(self):
        pass

