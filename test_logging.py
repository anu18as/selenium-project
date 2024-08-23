import logging


def test_loggingDemo():
    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler("logfile.log")
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)  # filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statment is executed")
    logger.info("Information statment")
    logger.warning("something is in warning mode")
    logger.error("A major error happened")
    logger.critical("critical issue")
