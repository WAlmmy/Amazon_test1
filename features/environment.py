from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from PageObject.Pages.BasePage import BasePage
from PageObject.Pages.HomePage import HomePage

def before_all(context):
    print("in before feature\n")
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(ChromeDriverManager().install())
    base_page = BasePage(driver)
    context.homepage = HomePage(base_page)