from PageObject.Locators import Locator
#from selenium.webdriver.support import Select
from selenium.webdriver.common.by import By
#from selenium import webdriver


class BasePage(object):

    def __init__(self, driver, base_url="amazon.co.uk"):
        self.driver= driver
        self.base_url=base_url
        #self.driver.implicitly_wait(10)
        #self.cart_count_span = driver.find_element(By.XPATH, Locator.cart_count_span)
    
    def find_byXpath(self,locator):
        return self.driver.find_element(By.XPATH, locator)
    
    