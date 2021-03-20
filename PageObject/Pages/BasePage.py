from PageObject.Locators import Locator
#from selenium.webdriver.support import Select
from selenium.webdriver.common.by import By
#from selenium import webdriver


class BasePage(object):

    def __init__(self, driver):
        self.driver= driver
        self.cart_count_span = driver.find_element(By.XPATH, Locator.cart_count_span)
    
    