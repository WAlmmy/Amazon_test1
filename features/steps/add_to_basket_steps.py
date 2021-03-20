from behave import given, when, then
from selenium import webdriver
from PageObject.Pages import *


@given(u'the user\'s basket has 0 items in it')
def step_impl(context):
    print("in initial scenario")
    #context.driver.get("https://www.amazon.co.uk/")
    page = context.homepage.go_to_page()
    print("In amazon.co.uk")
    #assert 
    #raise NotImplementedError(u'STEP: Given the user\'s basket has 0 items in it')


@when(u'the user adds the item to the basket')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user adds the item to the basket')


@then(u'the user\'s basket has 1 items in it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user\'s basket has 1 items in it')


@given(u'the user\'s basket has at least 1 item')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the user\'s basket has at least 1 item')


@then(u'the user\'s basket has one more item in it')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the user\'s basket has one more item in it')
