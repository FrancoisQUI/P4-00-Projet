from abc import ABC
import logging


class Controller(ABC):
    logger = logging.getLogger('app_log')

    def __init__(self, logger=logger):
        self.logger = logger

