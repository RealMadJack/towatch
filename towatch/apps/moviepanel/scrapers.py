import logging
import inspect
import mechanicalsoup
import os
import random
import sys
import time
import threading

from datetime import datetime


class IMDBScraper:
    """
    IMDB search-scrap movie rank and general info
    """

    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')

    def run(self):
        logging.info(f'Starting {self.__class__.__name__}')


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)-24s: %(levelname)-8s %(message)s')
    start = datetime.now()

    imdb_scraper = IMDBScraper()
    imdb_scraper.run()

    finish = datetime.now() - start
    logging.info(f'Done in: {finish}')


if __name__ == '__main__':
    main()
