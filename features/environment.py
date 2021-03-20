from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.Pages.BasePage import BasePage
from PageObject.Pages.HomePage import HomePage
import time

def before_all(context):
    print("in before feature\n")
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    time.sleep(1) #!!REMOVE!!
    print("driver created")
    #driver.get("amazon.co.uk")
    base_page = BasePage(driver)
    print("Base page")
    context.homepage = HomePage(base_page)
    print("Home page")