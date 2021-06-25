#! /usr/bin/env python3
# coding: utf-8
import logging

from Controllers import MainController




def main():
    # Initialize logging level
    logger = logging.getLogger('app_log')
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('app_logs.log')
    fh.setLevel(logging.DEBUG)
    logger.addHandler(fh)
    logger.info("J'entre dans main()")
    logger.info("Start APP")
    app = MainController.MainController()
    logger.info("Finish APP")

\
if __name__ == '__main__':
    main()
