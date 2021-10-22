from behave import *
from hamcrest import assert_that, equal_to, close_to
import logging

logformat="%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logging.basicConfig(filename='./do_some_logging.log',level=logging.DEBUG,format=logformat)

@given(u'the logfile is specified and initialised')
def step_impl(context):
    logging.info("The program has started")

@when(u'an error occurs')
def step_impl(context):
    context.errormessage = "Beautiful error message"

@then(u'this error gets logged to the logfile')
def step_impl(context):
    logging.debug(context.errormessage)

