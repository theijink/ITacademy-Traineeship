def after_all(context):
    try:
        context.browser.quit()
    except:
        pass