""" helper for logging"""

import logging
from config import Conf

default_logs = {
    'AllLogs': 'YES',
    'InfoLogs': 'YES',
    'ErrorLogs': 'YES',
    'WarningLogs': 'YES',
    'AllPrint': 'YES',
    'InfoPrint': 'YES',
    'ErrorPrint': 'YES',
    'WarningPrint': 'YES',
    }

path = "logs/"
format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

glob_config = Conf(__file__)
glob_config.chk_add_key_data('ALL_MODULES_LOGS', default_logs)
glob_conf = glob_config['ALL_MODULES_LOGS']
print(glob_conf['AllLogs'])

Green = '\033[92m'
Yellow = '\033[93m'
Red = '\033[91m'
Styles_end = '\033[0m'

"""TODO 
Вынести проврку директории и файлов в отдельный хелпер
fh вынести в отдельнуж функцию
"""


def create_logger(unit_name, log_type):
    logger = logging.getLogger(f'{log_type}_{unit_name}')
    fh = logging.FileHandler(f"{path}{log_type}_{unit_name}.log")
    fh.setFormatter(logging.Formatter(format))
    logger.addHandler(fh)
    return logger


class Logger:
    def __init__(self, name):
        self.info_logger = None
        self.err_logger = None
        self.warn_logger = None

        config = Conf(name)
        config.chk_add_key_data('LOGS', default_logs)
        self.conf = config['LOGS']

        if glob_conf['AllLogs'].upper() == 'NO' or self.conf['AllLogs'].upper() == 'NO':
            return

        if glob_conf['InfoLogs'].upper() == "YES" and self.conf['InfoLogs'].upper() == 'YES':
            self.info_logger = create_logger(name, 'info')
            self.info_logger.setLevel(logging.INFO)

        if glob_conf['ErrorLogs'].upper() == "YES" and self.conf['ErrorLogs'].upper() == 'YES':
            self.err_logger = create_logger(name, 'err')
            self.err_logger.setLevel(logging.ERROR)

        if glob_conf['WarningLogs'].upper() == "YES" and self.conf['WarningLogs'].upper() == 'YES':
            self.warn_logger = create_logger(name, 'warn')
            self.warn_logger.setLevel(logging.WARNING)

    def print_log(self, message):
        if glob_conf['AllPrint'].upper() == 'NO' or self.conf['AllPrint'].upper() == 'NO':
            return
        print(f'{message}{Styles_end}')

    def info(self, msg):
        if glob_conf['InfoPrint'].upper() == "YES" and self.conf['InfoPrint'].upper() == 'YES':
            self.print_log(f'{Green}{msg}')
        if self.info_logger is not None:
            print('try to save')
            self.info_logger.info(msg)

    def err(self, msg):
        if glob_conf['ErrorPrint'].upper() == "YES" and self.conf['ErrorPrint'].upper() == 'YES':
            self.print_log(f'{Red}{msg}')
        if self.err_logger is not None:
            self.err_logger.error(msg)

    def warn(self, msg):
        if glob_conf['WarningPrint'].upper() == "YES" and self.conf['WarningPrint'].upper() == 'YES':
            self.print_log(f'{Yellow}{msg}')
        if self.warn_logger is not None:
            self.warn_logger.warning(msg)


if __name__ == "__main__":
    log = Logger(__name__)
    log.info('INFO_NEW test message')
    log.err('ERR_NEW test message')
    log.warn('WARN_NEW test message')
