from behave import given, when, then
from selenium import webdriver
from utils import data_utils
from PageObject.Pages import *


@given(u'a user is viewing their basket')
def step_impl(context):
    context.basket.go_to_page()
    #raise NotImplementedError(u'STEP: Given a user is viewing their basket')


@when(u'the user changes the quantity of one of the items')
def step_impl(context):
    #
    context.initial_amount=context.basket.get_item_quantity()
    print("initial_amount: "+str(context.initial_amount))

    max_quantity=context.basket.get_max_quantity()
    print("max_quantitiy"+ str(max_quantity))
    new_amount=context.initial_amount
    print("new amount"+ str(new_amount))

    while new_amount==context.initial_amount:
        new_amount=data_utils.get_random_item_num(min=1, max=max_quantity)
        print("new amount"+ str(new_amount))


    context.basket.change_item_quantity(new_amount)
    print("quantity: "+ str(new_amount))


    #raise NotImplementedError(u'STEP: When the user changes the quantity of one of the items')


@then(u'the item quantity changes accordingly')
def step_impl(context):
    item_num=context.item.get_cart_count()
    assert item_num==context.initial_amount
    #raise NotImplementedError(u'STEP: Then the item quantity changes accordingly')


@then(u'the overall number of items in the basket changes accordingly')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the overall number of items in the basket changes accordingly')


@when(u'the user deletes an items')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user deletes an items')


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