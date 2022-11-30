import logging
import os
import datetime


class Log:
    _log = None

    def __new__(cls, *args, **kwargs):
        if cls._log is None:

            print("Log terbuat")
            cls._log = super().__new__(cls, *args, **kwargs)
            cls._log = logging.getLogger("crumbs")
            cls._log.setLevel(logging.DEBUG)
            formatter = logging.Formatter(
                '%(asctime)s [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            now = datetime.datetime.now()
            dirname = "./log"

            if not os.path.isdir(dirname):
                os.mkdir(dirname)
            fileHandler = logging.FileHandler(
                dirname + "/log_" + now.strftime("%Y-%m-%d")+".log")

            streamHandler = logging.StreamHandler()

            fileHandler.setFormatter(formatter)
            streamHandler.setFormatter(formatter)

            cls._log.addHandler(fileHandler)
            cls._log.addHandler(streamHandler)

        return cls._log


# a simple usecase
if __name__ == "__main__":
    logger = Log()
    logger.info("Log terbuat")
    logger = Log()
    logger.debug("bug occured")
