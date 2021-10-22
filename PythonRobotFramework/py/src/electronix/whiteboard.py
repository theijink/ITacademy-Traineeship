from behave import *
import requests

def aqcuire_data(var, Uk, Ub, Ri, Rl, I):
    URL = "http://dingdata.nl/batterij?"
    if var == 'Uk' and not None in [Ub, Ri, Rl]:    # calculate Uk
        #Uk = (Ub - (Ri * (Ub/(R+Rl))))
        #URL+="UB={}&RI={}&RL={}".format(Ub,Ri,Rl)
        return requests.get(url=URL, params={'UB':Ub, 'RI':Ri, 'RL':Rl}).json()['resultaten']['Uk']
    elif var == 'Ri' and not None in [Uk, Ub, Rl]:  # calculate Ri
        #Ri = ((Ub-Uk)/(Uk/Rl))
        #URL+="UB={}&UK={}&RL={}".format(Ub,Uk,Rl)
        return requests.get(url=URL, params={'UB':Ub, 'UK':Uk, 'RL':Rl}).json()['resultaten']['Ri']
    elif var == 'I' and not None in [Uk, Rl]:        # calculate I
        #I=Uk/Rl
        #URL+="UK={}&RL={}".format(Uk,Rl)
        return requests.get(url=URL, params={'UK':Uk, 'RL':Rl}).json()['resultaten']['I']
    elif var == 'Rl' and not None in [Uk, I]:       # calculate Rl
        #Rl=Uk/I
        #URL+="UK={}&I={}".format(Uk,I)
        return requests.get(url=URL, params={'UK':Uk, 'I':I}).json()['resultaten']['Rl']
    else:                                               # establish connection
        return requests.get(url=URL).json()['status']

def calculate_data(var, Uk, Ub, Ri, Rl, I):
    URL = "http://dingdata.nl/batterij?"
    if var == 'Uk' and not None in [Ub, Ri, Rl]:    # calculate Uk
        Uk = (Ub - (Ri * (Ub/(Ri+Rl))))
        #URL+="UB={}&RI={}&RL={}".format(Ub,Ri,Rl)
        #return requests.get(url=URL, params={'UB':Ub, 'RI':Ri, 'RL':Rl}).json()['resultaten']['Uk']
        return Uk
    elif var == 'Ri' and not None in [Uk, Ub, Rl]:  # calculate Ri
        Ri = ((Ub-Uk)/(Uk/Rl))
        #URL+="UB={}&UK={}&RL={}".format(Ub,Uk,Rl)
        #return requests.get(url=URL, params={'UB':Ub, 'UK':Uk, 'RL':Rl}).json()['resultaten']['Ri']
        return Ri
    elif var == 'I' and not None in [Rl, Uk]:        # calculate I
        I=Uk/Rl
        #URL+="UK={}&RL={}".format(Uk,Rl)
        #return requests.get(url=URL, params={'UK':Uk, 'RL':Rl}).json()['resultaten']['I']
        return I
    elif var == 'Rl' and not None in [Uk, I]:       # calculate Rl
        Rl=Uk/I
        #URL+="UK={}&I={}".format(Uk,I)
        #return requests.get(url=URL, params={'UK':Uk, 'I':I}).json()['resultaten']['Rl']
        return Rl
    else:                                               # establish connection
        #return requests.get(url=URL).json()['status']
        return 'invalid'

if True:
    URL = "http://dingdata.nl/batterij?"
    Ub, Uk, Rl = 5, 6, 3
    Ri = requests.get(url=URL, params={'UB':Ub, 'UK':Uk, 'RL':Rl}).json()#['resultaten']['Ri']
    print(Ri)

if False: ## determine values  for test
    test = (calculate_data('test', Uk=None, Ub=None, Ri=None, Rl=None, I=None))
    print(test)
    Ub, Ri, Rl = 6,3,9
    Uk = (calculate_data('Uk', Uk=None, Ub=Ub, Ri=Ri, Rl=Rl, I=None))
    print('Uk=',Uk, 'Ub=',Ub, 'Ri=',Ri, 'Rl=',Rl)

    Uk, Ub, Rl = 5, 3, 6
    Ri = (calculate_data('Ri', Uk=Uk, Ub=Ub, Ri=None, Rl=Rl, I=None))
    print('Ri=',Ri, 'Uk=',Uk, 'Ub=',Ub, 'Rl=',Rl)

    Uk, Rl = 6, 5
    I = (calculate_data('I', Uk=7, Ub=None, Ri=None, Rl=5, I=5))
    print('I=', I, 'Uk=', Uk, 'Rl=', Rl)

    Uk, Ri, = 3, 8
    Rl = (calculate_data('Rl', Uk=4, Ub=None, Ri=None, Rl=8, I=3))
    print('Rl=', Rl, 'Uk=', Uk, 'Ri=', Ri)
