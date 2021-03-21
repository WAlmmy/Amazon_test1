from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.Pages.BasePage import BasePage
from PageObject.Pages.HomePage import HomePage
from PageObject.Pages.ItemPage import ItemPage
from PageObject.Pages.BasketPage import BasketPage
from utils import data_utils
#import time

def before_all(context):
    # Get item list
    global item_list
    item_list = data_utils.get_item_list("ref/item_list.csv")
    print(item_list)
    print("in before feature\n")
    #driver = webdriver.Chrome()
    driver_install_dir=ChromeDriverManager().install()
    driver = webdriver.Chrome(driver_install_dir)
    driver.maximize_window()
    #
    # time.sleep(1) #!!REMOVE!!
    print("driver created")
    #driver.get("amazon.co.uk")
    base_page = BasePage(driver)
    print("Base page")
    context.homepage = HomePage(base_page)
    print("Home page")
    context.item = ItemPage(base_page, data_utils.get_random_element(item_list))
    context.basket=BasketPage(base_page)
    
def after_step(context, step):
    if step.status == "failed":
        print(context.scenario.name + " " + step.name)