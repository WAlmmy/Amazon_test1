from PageObject.Locators import Locator
from selenium.webdriver.common.by import By


class BasePage(object):

    def __init__(self, driver, base_url="amazon.co.uk"):
        self.driver= driver
        self.base_url=base_url
        self.cart_count_span=Locator.cart_count_span
    
    def find_byXpath(self,locator, element=None):
        if element is None:
            element=self.driver
        return element.find_element(By.XPATH, locator)

    def find_all_byXpath(self,locator, element=None):
        if element is None:
            element=self.driver
        return element.find_elements(By.XPATH, locator)
    
    def go_to_page(self):
        self.driver.get(self.base_url)
    
    def get_cart_count(self):
        try:
            cart_count=self.find_byXpath(self.cart_count_span)
        except:
            try:
                time.sleep(1)
                cart_count=self.find_byXpath(self.cart_count_span)
            except:
                print("Error getting cart count")
       
        return int(cart_count.text)
    
    