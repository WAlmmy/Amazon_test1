from behave import given, when, then
from selenium import webdriver
from utils import data_utils
from PageObject.Pages import *
import time


@given(u'a user is viewing their basket')
def step_impl(context):
    context.basket.go_to_page()
    #raise NotImplementedError(u'STEP: Given a user is viewing their basket')


@when(u'the user changes the quantity of one of the items')
def step_impl(context):
    #
    context.initial_item_amount=context.basket.get_item_quantity()
    print("initial item amount: "+str(context.initial_item_amount))

    context.initial_basket_amount=context.basket.get_cart_count()
    print("initial basket amount: "+str(context.initial_basket_amount))

    max_item_quantity=context.basket.get_max_quantity()
    print("max item quantitiy "+ str(max_item_quantity))
    context.new_item_amount=context.initial_item_amount
    print("new item amount: "+ str(context.new_item_amount))

    while context.new_item_amount==context.initial_item_amount or context.new_item_amount>9:
        context.new_item_amount=data_utils.get_random_item_num(min=1, max=max_item_quantity)
        print("new item amount: "+ str(context.new_item_amount))

    context.item_number_diff=context.new_item_amount-context.initial_item_amount
    print("item number diff: "+ str(context.item_number_diff))

    # !! Issue; Cannot locate option with value: 11
    context.basket.change_item_quantity(context.new_item_amount)
    print("item quantity: "+ str(context.item_number_diff))


    #raise NotImplementedError(u'STEP: When the user changes the quantity of one of the items')


@then(u'the item quantity changes accordingly')
def step_impl(context):
    print("checking item quantity...")
    item_num=context.basket.get_item_quantity()
    print("then: item quantity check: "+ str(item_num))
    assert item_num==context.new_item_amount
    #raise NotImplementedError(u'STEP: Then the item quantity changes accordingly')


@then(u'the overall number of items in the basket changes accordingly')
def step_impl(context):
    time.sleep(1)
    basket_item_num=context.basket.get_cart_count()
    print("then: basket quantity check: "+ str(basket_item_num))
    calc_basket_total=context.initial_basket_amount+context.item_number_diff
    print("calculated basket total "+ str(calc_basket_total))
    print("Basket item num "+ str(basket_item_num))
    
    assert basket_item_num == calc_basket_total
    #raise NotImplementedError(u'STEP: Then the overall number of items in the basket changes accordingly')


@when(u'the user deletes an item')
def step_impl(context):
    context.basket.save_item_list()
    context.item_to_delete=data_utils.get_random_element(context.basket.saved_item_list)
    print("length of current list: "+str(len(context.basket.get_items_in_basket())))
    print("length of saved list: " +str(len(context.basket.saved_item_list)))
    time.sleep(3)

    #raise NotImplementedError(u'STEP: When the user deletes an items')


@then(u'the item is no longer present in the basket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the item is no longer present in the basket')


@when(u'the user deletes all items')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user deletes all items')


@then(u'no items are present in the basket')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then no items are present in the basket')


@then(u'a message saying the basket is empty is displayed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then a message saying the basket is empty is displayed')