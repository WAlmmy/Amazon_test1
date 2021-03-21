from PageObject.Locators import Locator
#from selenium.webdriver.support import Select
from selenium.webdriver.common.by import By
#from selenium import webdriver


class BasePage(object):

    def __init__(self, driver, base_url="amazon.co.uk"):
        self.driver= driver
        self.base_url=base_url
        self.cart_count_span=Locator.cart_count_span
        #self.driver.implicitly_wait(10)
        #self.cart_count_span = driver.find_element(By.XPATH, Locator.cart_count_span)
    
    def find_byXpath(self,locator, element=None):
        if element is None:
            element=self.driver
        return element.find_element(By.XPATH, locator)
    
    def go_to_page(self):
        print("going to: " + self.base_url)
        self.driver.get(self.base_url)
    
    def get_cart_count(self):
        cart_count=self.find_byXpath(self.cart_count_span)
        print(cart_count)
        return int(cart_count.text)
    
    