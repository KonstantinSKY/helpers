""" helper for logging"""

import logging
from config import Conf

Green = '\033[92m'
Red = '\033[91m'
Styles_end = '\033[0m'

class Logger:
    def __init__(self, name):
        # self.err_logger = logging.getLogger(f'err_{name}')
        # self.info_logger = logging.getLogger(f'info_{name}')
        #
        # self.err_logger.setLevel(logging.ERROR)
        # self.info_logger.setLevel(logging.INFO)
        #
        # fh_err = logging.FileHandler(f"logs/err_{name}.log")
        # fh_info = logging.FileHandler(f"logs/info_{name}.log")
        #
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # fh_err.setFormatter(formatter)
        # fh_info.setFormatter(formatter)
        #
        # self.err_logger.addHandler(fh_err)
        # self.info_logger.addHandler(fh_info)
        #
        # self.allow_log = True
        # self.allow_print = True

    def prn_info(self, msg):
        if self.allow_print:
            print(f'{Green}{msg}{Styles_end}')

    def prn_err(self, msg):
        if self.allow_print:
            print(f'{Red}{msg}{Styles_end}')

    def log_err(self, msg):
        if self.allow_log:
            self.err_logger.error(msg)

    def log_info(self, msg):
        if self.allow_log:
            self.info_logger.info(msg)

    def prn_log_err(self, msg):
        self.log_err(msg)
        self.prn_err(msg)

    def prn_log_info(self, msg):
        self.log_info(msg)
        self.prn_info(msg)


if __name__ == "__main__":
    # log = Logger(__name__)
    # log.prn_log_info('Green')
    # log.prn_log_err('Red')
