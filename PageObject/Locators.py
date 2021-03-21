
class Locator(object):

    basket = "//a[@id=nav-cart]"
    cart_count_span = "//*[@id='nav-cart-count']"
    add_to_cart_button="//input[@id='add-to-cart-button']"
    item_quantity="//select[@id='quantity']"
    #basket_item_quantity="//select[@name='quantity']"
    basket_item_quantity="//select[@class='a-native-dropdown a-declarative sc-update-quantity-select']"
    #basket_item="//div[@class='a-link-normal sc-product-link']"
    #basket_item="//div[@data-quantity]"
    basket_item="//div[@class='a-row sc-list-item sc-list-item-border sc-java-remote-feature']"
    item_delete="//input[@value='Delete']"
    item_removed_message="//div[@class='sc-list-item-removed-msg']"
    removed_basket_item_title="//a[@class='a-link-normal sc-product-link']"
    existing_basket_item_title="//a[@class='a-link-normal sc-product-link']"
    #existing_basket_item_title="//span[@class='a-size-medium sc-product-title a-text-bold']"
    existing_basket_item_image="//img"
    removed_basket_item_span="//span[text()='was removed from Shopping Basket.']"
    all_anchors="//a[@href]"

