import behave
def before_all(context):
    import logging
    logformat="%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
    logging.basicConfig(filename='./do_some_logging.log',level=logging.DEBUG,format=logformat)

