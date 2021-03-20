from PageObject.Locators import Locator
from selenium.webdriver.support import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

class Basket(object):

    def __init__(self, driver):
        self.driver=driver

    def delete_item(self,item):
        pass