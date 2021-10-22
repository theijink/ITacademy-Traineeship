from behave import *

@given(u'there is an empty text file available to us')
def step_impl(context):
    context.filename="empty_file"
    context.f = open(context.filename, "wt")
    context.f.close()
    assert context.f.name is context.filename

@when(u'I open this file')
def step_impl(context):
    context.f = open(context.filename, "at")
    #assert True
    #assert context.f.name is context.filename

@when(u'I write the following table in it')
def step_impl(context):
    for row in context.table:
        line=''
        for item in row:
            line+=item+'\t'
        context.f.write(line+'\n')
    context.f.close()
    #assert True

@then(u'this file has three lines in it')
def step_impl(context):
    context.f = open(context.filename, 'r')
    lines = len([i for i in context.f])
    context.f.close()
    assert lines>=0

@given(u'the text file has been opened')
def step_impl(context):
    context.filename="another_file"
    context.f = open(context.filename, "at")
    context.f.close()
    assert context.f.name is context.filename

@then(u'I write the values {one}, {two} and {three}')
def step_impl(context, one, two, three):
    context.f = open(context.filename, 'at')
    line=''
    for item in [one, two, three]:
        line+=item+'\t'
    context.f.write(line+'\n')
    context.f.close()
    assert True

@then(u'I close the file')
def step_impl(context):
    context.f = open(context.filename, 'r')
    context.f.close
    print('closed')
    assert True
