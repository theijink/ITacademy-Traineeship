### preconditions ###
To be able to make use of the behave automatisation tool, few prerequisities are necessasry. It is recommended to use a virual environment. Here, some python dependencies need to be installed. The behave extension requires a given directory structure.

# setup virtual environment
$ pip install virtualenv                # install venv
$ python3 -m venv <name>                # create venv
$ source <name>/bin/activate            # activate venv

# install dependencies
$ pip install behave                    # cucumber
$ pip install selenium                  # web server + client
$ pip install splinter                  # 
$ pip install pyhamcrest                # 
$ pip install logging                   # 
$ pip install requests                  # 

# create directory structure and files
$ mkdir features                        # mandatory dirname
$ mkdir features/steps                  # mandatory dirname
$ touch features/<featurename>.feature  # mandatory extension
$ touch features/steps/<stepname>.py    # mandatory extension
$ touch features/environment.py         # ONLY py file in /features

# placeholder usage for re-usable functions
@given('the switch is in position {pos}')
def step_impl(context, pos):
    set_witch_in_position(pos)

# optional functions in the environment.py module
import ...
before_step(context, step)
after_step(context, step)
before_scenario(context, scenario)
after_scenario(context, scenario)
before_feature(context, feature)
after_feature(context, feature)
before_tag(context, tag)
after_tag(context, tag)
before_all(context)
after_all(context)

# tags within the feature
create a feature file with tags e.g. 
    @regression
    Scenario:...
    Given ...
    Then ...
$ behave --tags=regression, .., etc

### assessment ###
- environment.py includes information
- behave will look in ALL python files in /steps to find the function. 
- Make steps as multi-useable as possible
- steps are identified using decorators @given, @when, or @then
- after the decorator follows ('<line in feature file>'). This is copied exactly!
- function names (like step_impl) are important and might be re-used and re-named
- context is the place at which data is stored, e.g. variable values. It'll get stored until the next scenario
- context.table is where datatables are stored: for row in context.table: row['first']=...; row['second']=...; etc. so a dictionary
- context.text is where the multiline doctring gets stored
- context.failed stores any failed step
- context.<variable> is a way to create a new variable to pass within scenario






