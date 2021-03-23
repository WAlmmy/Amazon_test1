from behave import given, when, then
from selenium import webdriver
from utils import data_utils
from PageObject.Pages import *
import time


@given(u'a user is viewing their basket')
def step_impl(context):
    context.basket.go_to_page()


@when(u'the user changes the quantity of one of the items')
def step_impl(context):
    context.initial_item_amount=context.basket.get_item_quantity()
    context.initial_basket_amount=context.basket.get_cart_count()
    max_item_quantity=context.basket.get_max_quantity()
    context.new_item_amount=context.initial_item_amount
    while context.new_item_amount==context.initial_item_amount or context.new_item_amount>9:
        context.new_item_amount=data_utils.get_random_item_num(min=1, max=max_item_quantity)
    context.item_number_diff=context.new_item_amount-context.initial_item_amount
    context.basket.change_item_quantity(context.new_item_amount)


@then(u'the item quantity changes accordingly')
def step_impl(context):
    item_num=context.basket.get_item_quantity()
    assert item_num==context.new_item_amount


@when(u'the user deletes an item')
def step_impl(context):
    context.basket.save_item_list()
    context.item_to_delete=data_utils.get_random_element(context.basket.saved_item_list)
    context.item_number_diff=context.basket.get_item_quantity(context.item_to_delete)*(-1)
    context.initial_basket_amount = context.basket.get_cart_count()
    context.selected_item_ID=context.basket.get_existing_item_product_ID(context.item_to_delete)
    context.basket.delete_item(context.item_to_delete)


@then(u'the overall number of items in the basket changes accordingly')
def step_impl(context):
    time.sleep(1)
    basket_item_num=context.basket.get_cart_count()
    calc_basket_total=context.initial_basket_amount+context.item_number_diff
    
    assert basket_item_num == calc_basket_total


@then(u'the item is no longer present in the basket')
def step_impl(context):
    removed_item_ID=context.basket.get_removed_item_product_ID()

    assert removed_item_ID == context.selected_item_ID


@when(u'the user deletes all items')
def step_impl(context):
    item_list=context.basket.get_items_in_basket()
    for i in range(0,len(item_list)):
        try:
            context.basket.delete_item(context.basket.driver)
        except:
            time.sleep(1.5)
            try:
                context.basket.delete_item(context.basket.driver)
            except:
                print("Error deleting item")
                #raise Exception("Error deleting item")
    

@then(u'no items are present in the basket')
def step_impl(context):
    assert context.basket.get_cart_count()==0


@then(u'a message saying the basket is empty is displayed')
def step_impl(context):
    time.sleep(2)
    message=context.basket.get_cart_empty_message()
    assert "Your Amazon basket is empty" in message
    