from logger import logging

def calc(a,b):
    logging.debug("Adding")
    return a+b

logging.debug("Addion completed")
calc(2,4)