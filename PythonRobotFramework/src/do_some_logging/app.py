import logging

logformat="%(levelname)s:%(filename)s:%(lineno)d:%(asctime)s:%(message)s"
logging.basicConfig(filename='./app.log',level=logging.DEBUG,format=logformat)
logging.info("The program has started")

logging.debug("Setting the value of a")
a = [0,1,2,3,4,5,6]

logging.debug("Starting the loop")
for b in a:
    logging.debug("Fetching %s", b)

logging.debug("Through the loop")

logging.info("Last line of code has passed.")