#! /usr/bin/env python3
# coding: utf-8
import logging
from Core.variables_settings import LOG_FILENAME

from Controllers import MainController


def main():
    def init_logger():
        _logger = logging.getLogger('app_log')
        _logger.setLevel(logging.DEBUG)
        _file_handler = logging.FileHandler(LOG_FILENAME)
        _file_handler.setLevel(logging.DEBUG)
        _formatter = logging.Formatter('%(asctime)s-'
                                       '%(levelname)s : '
                                       '%(message)s')
        _file_handler.setFormatter(_formatter)
        _logger.addHandler(_file_handler)
        return _logger

    logger = init_logger()

    logger.info("Start APP")
    app = MainController.MainController()
    logger.info("Finish APP")


if __name__ == '__main__':
    main()
