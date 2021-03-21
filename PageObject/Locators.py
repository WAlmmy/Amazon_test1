
class Locator(object):

    basket = "//a[@id=nav-cart]"
    cart_count_span = "//*[@id='nav-cart-count']"
    add_to_cart_button="//input[@id='add-to-cart-button']"
    item_quantity="//select[@id='quantity']"
    #basket_item_quantity="//select[@name='quantity']"
    basket_item_quantity="//select[@class='a-native-dropdown a-declarative sc-update-quantity-select']"
    basket_item="//a[@class='a-link-normal sc-product-link']"
    item_delete="//input[@value='Delete']"