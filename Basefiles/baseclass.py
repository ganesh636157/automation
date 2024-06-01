import inspect
import logging

class baseclass1:
    def test_loggingDemo(self):
        looger_name=inspect.stack()[1][3]
        logger = logging.getLogger(looger_name)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  #filehandler object

        logger.setLevel(logging.DEBUG)
        return logger
    #logger.debug("A debug statement is executed")
    #logger.info("Information statement")
    #logger.debug("A debug statement is executed")
    #logger.warning("Something is in warning mode")
    #logger.error("A Major error has happend")
    #logger.critical("Critical issue")



