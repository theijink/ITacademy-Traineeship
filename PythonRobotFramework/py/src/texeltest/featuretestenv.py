from splinter.browser import Browser
import logging
from hamcrest import assert_that, equal_to, close_to
from time import sleep

def press_text_button(txt):
    try:
        button=browser.find_by_text(txt)[0]
        button.click()
    except:
        print('Unclickable', browser.find_by_text(txt)[0])

def mouse_over_text(txt):
    try:
        field=browser.find_by_text(txt)[0]
        field.mouse_over()
    except:
        print(browser.find_by_text(txt))

website="https://www.texel.net/en/"

browser=Browser()
url=website
browser.visit(url)

## cookie message [Accept]
txt='Accept'
press_text_button(txt)


if False:
    base = browser.links()#find_by_id("__name")
    try:
        for i in range(len(base)):
            print(i, '/', len(base), base[i])
    except:
        print(base)

if False: ## try out each button
    elements=browser.find_by_tag('button')
    for e in range(len(elements)):
        try:
            elements[e].click()
            sleep(1)
        except:
            print(e+1,'/', len(elements), elements[e])
        

if False: ## loop over header menu items

    textmenu = {
        "what's on":[],
        "See and do":["One and a half meters on Texel", "Outdoor activities & Sports", "Food and drink", "Arts and culture", "Activities for children", "Shopping", "Holiday tips", "Webcams on Texel", "Activities for disabled persons", "The Texel holiday feeling at home", "Activities for dog owners", "Activities for groups", "Wellness"],
        "To Texel":[],
        "Accomodations":[],
        "About Texel":[],
    }

    for head in textmenu:
        mouse_over_text(head)
        sleep(1)
        for line in textmenu[head]:
            #mouse_over_text(line)
            press_text_button(line)
            sleep(1)

if True:

    for tag in ['svg', 'h1', 'h2', 'h3', 'h4', 'h5', 'button']:
        list = browser.find_by_tag(tag)
        for i in range(len(list)):
            #browser.visit(url)
            item=list[i]
            print('{}/{} testing {}'.format(i+1,len(list), item))
            try:
                item.mouse_over()
                sleep(1)
            except:
                print('Unable to "mouse over" this item')
            #try:
            #    item.click()
            #    sleep(1)
            #except:
            #    print('Unable to click on this item')




sleep(1)
browser.quit()