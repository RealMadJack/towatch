import sys
import os
import django

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__name__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()


import logging
import inspect
import mechanicalsoup
import random
import time
import threading

from datetime import datetime
from imdb import IMDb
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
        logging.info(f'- Calling {inspect.stack()[0][3]} module')
        movies = Movie.objects.filter(is_scraped=False)
        return movies

    def create_movie_queue(self):
        pass

    def search_imdb_movie(self, movie):
        imdb = IMDb()
        result = imdb.search_movie(movie.name)
        return result

    def run(self):
        """
        Queue, threading cycle
        """
        filtered_movies = self.get_filter_db_movies()

        for movie in filtered_movies[:2]:
            imdb_search_list = self.search_imdb_movie(movie)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)-24s: %(levelname)-8s %(message)s')
    start = datetime.now()

    imdb_scraper = IMDBScraper()
    imdb_scraper.run()

    finish = datetime.now() - start
    logging.info(f'Done in: {finish}')


if __name__ == '__main__':
    main()
