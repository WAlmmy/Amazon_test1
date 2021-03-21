from behave import given, when, then
from selenium import webdriver
from PageObject.Pages import *
from utils import data_utils
from PageObject.Pages.ItemPage import ItemPage
from decouple import config

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
    print("cart_count" + str(context.item.get_cart_count()))
    assert context.item.get_cart_count()==1
    print("after assert")
    #raise NotImplementedError(u'STEP: Then the user\'s basket has 1 items in it')


@given(u'the user\'s basket has at least 1 item')
def step_impl(context):
    print("in user has at least 1 item in basket...")
    context.homepage.go_to_page()
    context.start_cart_count=context.homepage.get_cart_count()
    print(context.start_cart_count)
    if context.start_cart_count<1:
        #Check and reset if Scenario 1 fails
        context.item.go_to_page()
        max_quantity=context.item.get_max_quantity()
        new_amount=data_utils.get_random_item_num(min=1, max=max_quantity)
        context.item.change_item_quantity(new_amount)
        print("quantity: "+ str(new_amount))
        context.item.add_item_to_cart()
        context.start_cart_count=context.item.get_cart_count()

    print("context.start_cart_count: "+ str(context.start_cart_count))
    context.start_cart_count
    assert context.start_cart_count >= 1
    #raise NotImplementedError(u'STEP: Given the user\'s basket has at least 1 item')


@then(u'the user\'s basket has one more item in it')
def step_impl(context):
    assert context.item.get_cart_count() == context.start_cart_count+1
    #raise NotImplementedError(u'STEP: Then the user\'s basket has one more item in it')



@when(u'the user adds an item {X_times} to the basket')
def step_impl(context, X_times):
    X_times=int(X_times)
    item_list = data_utils.get_item_list(config("CSV_PATH"))
    for i in range(0,X_times):
        print("context.initial_item_url: "+ context.initial_item_url)
        print("context.item.get_item_url: "+ context.item.get_item_url())
        while context.initial_item_url==context.item.get_item_url:
            context.item=ItemPage(context.base_page, data_utils.get_random_element(item_list))
        context.item.go_to_page()
        context.item.add_item_to_cart()
    #raise NotImplementedError(u'STEP: When the user adds an item X times to the basket')


@then(u'the user\'s basket has {X_times} more items in it')
def step_impl(context,X_times):
    print("X_times "+X_times)
    print("context.start_cart_count "+str(context.start_cart_count))

    X_times=int(X_times)
    current_cart_count=context.item.get_cart_count()
    print("current_cart_count: "+str(current_cart_count))
    assert current_cart_count==context.start_cart_count+X_times
    #raise NotImplementedError(u'STEP: Then the user\'s basket has X more item in it')