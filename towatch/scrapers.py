import sys
import os
import environ
sys.path.append(os.path.join(environ.Path(__file__) - 2))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
import django
django.setup()

import logging
import inspect
import mechanicalsoup
import random
import time
import threading

from datetime import datetime

from towatch.apps.moviepanel.models import Movie


# http://www.omdbapi.com/
class IMDBScraper:
    """
    IMDB search-scrap movie rank and general info

    On model save if not is_scraped => run

    query movies => filter movies without info => create queue => add movies to queue
    => search imbd movie by the title => if found => visit first result uri => scrap data
                                      => if not => log result (in prod db table)
    => validate scraped data => save Movie object
    """

    def __init__(self, target_url='imdb.com'):
        logging.info(f'Creating instance: {self.__class__.__name__}')
        self.target_url = target_url

    def get_filter_db_movies(self):
        """
        if movie has imdb True, don't search
        """
        movies = Movie.objects.filter(is_scraped=False)
        return movies

    def create_movie_queue(self):
        pass

    def search_imdb_movie(self):
        pass

    def run(self):
        """
        Queue, threading cycle
        """
        filtered_movies = self.get_filter_db_movies()
        print(filtered_movies)

        # cycle trough que and search movie

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
