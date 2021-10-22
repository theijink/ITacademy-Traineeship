from behave import *
from splinter.browser import Browser
import logging
from time import sleep
from tkinter import messagebox


@given(u'the browser has been started up')
def step_impl(context):
    context.browser=Browser()
    sleep(1)
    
@then(u'visit the page for the engine')
def step_impl(context):
    context.browser.visit("https://duckduckgo.com")
    sleep(1)
    context.browser.quit()

@given(u'the home page of the engine has been openend')
def step_impl(context):
    context.browser=Browser()
    context.browser.visit("https://duckduckgo.com")
    sleep(1)

@when(u'I enter {something} in the entry')
def step_impl(context, something):
    context.text=something
    sleep(1)

@then(u'{something} must appear in the entry')
def step_impl(context, something):
    context.browser.fill('q', something)
    sleep(1)
    context.browser.quit()

@given(u'{something} is entered in the entry box')
def step_impl(context, something):
    context.browser=Browser()
    context.browser.visit("https://duckduckgo.com")
    context.browser.fill('q', something)
    sleep(1)
    
@given(u'a search button is shown')
def step_impl(context):
    context.button = context.browser.find_by_id('search_button_homepage')
    sleep(1)
    
@when(u'I press the search button')
def step_impl(context):
    context.button.click()
    sleep(1)
    
@then(u'the results must appear in the browser')
def step_impl(context):
    sleep(1)
    context.browser.quit()

@then(u'close the browser')
def step_impl(context):
    sleep(1)
    context.browser.quit()
