from behave import *
from splinter.browser import Browser
import logging
from hamcrest import assert_that, equal_to, close_to
import time as ts


@given(u'we are on {website}')
def step_impl(context, website):
    context.browser=Browser()
    context.url=website
    context.browser.visit(context.url)
    
    #context = close_cookie_window(context)

    cookiewindow=context.browser.getElementsByClassName('CookieConsent__Container-sc-hx5gyg-1 dFLtVj')

    ts.sleep(3)
    context.browser.quit()


def close_cookie_window(context):
    context.id="__next"
    context.element=Browser.find_by_id(context.id)
    button=context.element.getElementsByClassName('sc-gtsrHT cMZePO accept')
    button.click()
    return context


@given(u'the id of the header is {headerid}')
def step_impl(context, headerid):
    pass

@when(u'I click on {placeholder}')
def step_impl(context, placeholder):
    pass

@then(u'I want to be directed to {reference}')
def step_impl(context, reference):
    pass