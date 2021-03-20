from behave import given, when, then
from selenium import webdriver
from PageObject.Pages import *
from utils import data_utils


@given(u'the user\'s basket has 0 items in it')
def step_impl(context):
    print("in initial scenario")
    #context.driver.get("https://www.amazon.co.uk/")
    context.homepage.go_to_page()
    print("In amazon.co.uk")
    print(context.homepage.get_cart_count())
    assert context.homepage.get_cart_count()==0
    #assert 
    #raise NotImplementedError(u'STEP: Given the user\'s basket has 0 items in it')


@when(u'the user adds the item to the basket')
def step_impl(context):
    context.item.go_to_page()
    print("in item page")
    context.item.add_item_to_cart()

    #raise NotImplementedError(u'STEP: When the user adds the item to the basket')


@then(u'the user\'s basket has 1 items in it')
def step_impl(context):
    print("checking item count")
    print(context.item.get_cart_count())
    assert context.item.get_cart_count()==1
    print("after assert")
    #raise NotImplementedError(u'STEP: Then the user\'s basket has 1 items in it')


@given(u'the user\'s basket has at least 1 item')
def step_impl(context):
    print("in user has at least 1 item in basket...")
    context.homepage.go_to_page()
    item_num=context.homepage.get_cart_count()
    print(item_num)
    if item_num<1:
        #Check and reset if Scenario 1 fails
        context.item.go_to_page()
        max_quantity=context.item.get_max_quantity()
        new_amount=data_utils.get_random_item_num(min=1, max=max_quantity)
        context.item.change_item_quantity(new_amount)
        print("quantity: "+ str(new_amount))
        context.item.add_item_to_cart()
        item_num=context.item.get_cart_count()

    print("item num: "+ str(item_num))
    context.start_num = item_num
    assert item_num >= 1
    #raise NotImplementedError(u'STEP: Given the user\'s basket has at least 1 item')


@then(u'the user\'s basket has one more item in it')
def step_impl(context):
    assert context.item.get_cart_count() == context.start_num+1
    #raise NotImplementedError(u'STEP: Then the user\'s basket has one more item in it')
