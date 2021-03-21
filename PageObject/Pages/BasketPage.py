from PageObject.Locators import Locator
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils import data_utils
from .BasePage import BasePage

class BasketPage(BasePage):

    def __init__(self, context):
        self.add_to_cart_button=Locator.add_to_cart_button
        self.basket_item_quantity=Locator.basket_item_quantity
        self.item_delete= Locator.item_delete
        self.basket_item=Locator.basket_item
        self.item_removed_message=Locator.item_removed_message
        self.removed_basket_item_title=Locator.removed_basket_item_title
        self.existing_basket_item_title=Locator.existing_basket_item_title
        self.removed_basket_item_span=Locator.removed_basket_item_span
        self.all_anchors=Locator.all_anchors
        self.cart_empty=Locator.cart_empty
        BasePage.__init__(self, context.driver, base_url="https://www.amazon.co.uk/gp/cart/view.html?ref_=nav_cart")
        self.context=context

    def save_item_list(self):
        print("saving item list")
        self.saved_item_list=self.get_items_in_basket()
        

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
    
    def get_max_quantity(self, element=None):
        """
        Returns max quantity in item quanitity dropdown
        """
        print("getting max quantity...")
        if element is None:
            element=self.driver
        quantity_select=self._get_quantity_select()
        print(quantity_select)
        
        max_quantity=len(quantity_select.options)-1
        print("found max quantity...")
        return max_quantity

    def get_item_quantity(self, element=None):
        """
        Returns an integer of the quantity of an item
        """
        if element is None:
            element=self.driver
        quantity_select=self._get_quantity_select(element)
        selected_option = quantity_select.first_selected_option
        print("selected_option: " + str(selected_option))
        print("text: "+selected_option.text)
        print(type(selected_option.text))
        return int(selected_option.text)
    
    def _get_quantity_select(self, element=None):
        """
        returns a Select object of item quantity dropdown
        """
        if element is None:
            element=self.driver
        return Select(self.find_byXpath(self.basket_item_quantity, element=element))

    def get_items_in_basket(self):
        """
        returns a list of items in basket
        """
        return self.find_all_byXpath(self.basket_item)

    def delete_item(self,element):
        item_delete_button=self.find_byXpath(self.item_delete,element=element)
        #ActionChains(self.driver).click(element).perform()
        item_delete_button.click()

    def get_removed_item_title(self, element=None):
        if element is None:
            element=self.driver
        #basket_item=self.find_byXpath(self.item_removed_message,element)
        removed_item_span=self.get_removed_item_span(element)
        print(removed_item_span.text)
        #item_title=self.find_byXpath(self.removed_basket_item_title,basket_item).getAttribute("alt")
        removed_item_title=self.find_byXpath(self.get_removed_item_span,removed_item_span).get_attribute("text")
        print(removed_item_title)
        return removed_item_title
    
    def get_removed_item_product_ID(self, element=None):
        if element is None:
            element=self.driver
        removed_item_span=self.get_removed_item_span(element)
        #item_href=self.find_byXpath(self.removed_basket_item_title,removed_item_span).get_element("href")
        #removed_item_anchor=self.find_byXpath(self.all_anchors,removed_item_span)
        #locator doesn't work. Temporariliy using find element by tag name
        removed_item_anchor=removed_item_span.find_element_by_tag_name("a")
        item_href=removed_item_anchor.get_attribute("href")
        print(item_href)
        product_ID= data_utils.get_product_id_from_href(item_href)
        print(product_ID)
        return product_ID

    def get_existing_item_product_ID(self,element=None):
        if element is None:
            element=self.driver
        item_href=self.find_byXpath(self.existing_basket_item_title,element).get_attribute("href")
        product_ID= data_utils.get_product_id_from_href(item_href)
        print(product_ID)
        return product_ID

    def get_existing_item_title(self, element):
        print("getting existing item title...")
        item_title=self.find_byXpath(self.all_anchors,element).get_attribute("alt")
        print(item_title)
        return item_title

    def get_removed_item_span(self,element=None):
        if element is None:
            element=self.driver
        print("getting removed item span...")
        removed_item_span=self.find_byXpath(self.removed_basket_item_span, element)
        print(removed_item_span.text)
        #print(removed_item_span)
        return removed_item_span

    def get_cart_empty_message(self):
        cart_empty_span=self.find_byXpath(self.cart_empty)
        print(cart_empty_span.text)
        return cart_empty_span.text
