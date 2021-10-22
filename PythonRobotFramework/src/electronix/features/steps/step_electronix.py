from behave import *
from hamcrest import assert_that, equal_to, close_to
import requests

def aqcuire_data(var, Uk, Ub, Ri, Rl, I):
    URL = "http://dingdata.nl/batterij?"
    if var == 'Uk' and not None in [Ub, Ri, Rl]:        # calculate Uk
        return requests.get(url=URL, params={'UB':Ub, 'RI':Ri, 'RL':Rl}).json()['resultaten']['Uk']
    elif var == 'Ri' and not None in [Uk, Ub, Rl]:      # calculate Ri
        return requests.get(url=URL, params={'UB':Ub, 'UK':Uk, 'RL':Rl}).json()['resultaten']['Ri']
    elif var == 'I' and not None in [Uk, Rl]:           # calculate I
        return requests.get(url=URL, params={'UK':Uk, 'RL':Rl}).json()['resultaten']['I']
    elif var == 'Rl' and not None in [Uk, I]:           # calculate Rl
        return requests.get(url=URL, params={'UK':Uk, 'I':I}).json()['resultaten']['Rl']
    else:                                               # establish connection
        return requests.get(url=URL).json()['status']


@given(u'the battery calculation module is online and available')
def step_impl(context):
    context.connection=aqcuire_data(var=None, Uk=None, Ub=None, Ri=None, Rl=None, I=None)
    assert_that(context.connection, close_to('succes',0.1))

@when(u'I call the battery calculation module with Uk={Uk} and Rl={Rl}')
def step_impl(context, Uk, Rl):
    Uk=float(Uk)
    Rl=float(Rl)
    context.I = float(aqcuire_data(var='I', Uk=Uk, Ub=None, Ri=None, Rl=Rl, I=None))

@then(u'the module calculates the correct value of I={I}')
def step_impl(context, I):
    I=float(I)
    assert_that(context.I, close_to(I,0.1))

@when(u'I call the battery calculation module with Ub={Ub}, Ri={Ri}, and Rl={Rl}')
def step_impl(context, Ub, Ri, Rl):
    Ub=float(Ub)
    Ri=float(Ri)
    Rl=float(Rl)
    context.Uk = float(aqcuire_data(var='Uk', Uk=None, Ub=Ub, Ri=Ri, Rl=Rl, I=None))

@then(u'the module calculates the correct value of Uk={Uk}')
def step_impl(context, Uk):
    Uk=float(Uk)
    assert_that(context.Uk, close_to(Uk,0.1))

@when(u'I call the battery calculation module with Ub={Ub}, Uk={Uk}, and Rl={Rl}')
def step_impl(context, Ub, Uk, Rl):
    Ub=float(Ub)
    Uk=float(Uk)
    Rl=float(Rl)
    context.Ri=float(aqcuire_data(var='Ri', Uk=Uk, Ub=Ub, Ri=None, Rl=Rl, I=None))

@then(u'the module calculates the correct value of Ri={Ri}')
def step_impl(context, Ri):
    Ri=float(Ri)
    assert_that(context.Ri, close_to(Ri, 0.1))
    
@when(u'I call the battery calculation module with Uk={Uk} and I={I}')
def step_impl(context, Uk, I):
    Uk=float(Uk)
    I=float(I)
    Rl=float(aqcuire_data(var='Rl', Ub=None, Uk=Uk, Ri=None, Rl=None, I=I))    

@then(u'the module calculates the correct value for Rl={Rl}')
def step_impl(context, Rl):
    Rl=float(Rl)
    assert_that(context.Rl, close_to(Rl, 0.1))


