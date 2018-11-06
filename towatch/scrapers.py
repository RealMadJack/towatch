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


# Logging restrictions
logging.getLogger("imdbpy").setLevel(logging.WARNING)
logging.getLogger("imdb.parser.http.piculet").setLevel(logging.WARNING)


class IMDBScraper:
    """
    IMDB search-scrap movie rank and general info

    On model save if not is_scraped => run

    query movies => filter movies without info => create queue => add movies to queue
    => search imbd movie by the title => if found => visit first result uri => scrap data
                                      => if not => log result (in prod db table)
    => validate scraped data => save Movie object
    """

    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')
        self.imdb = IMDb()

    def get_filter_db_movies(self):
        logging.info(f'Calling {inspect.stack()[0][3]} module')
        movies = Movie.objects.filter(is_scraped=False)
        return movies

    def create_movie_queue(self):
        pass

    def search_imdb_movie(self, movie):
        result = self.imdb.search_movie(movie.name)
        return result

    def get_validate_search_list_movie(self, search_list, current_movie):
        logging.info(f'Calling {inspect.stack()[0][3]} module')

        # print(f'Current movie date: {current_movie.release_date}')
        # print(first_movie['year'])
        # print(first_movie['long imdb canonical title'])

        # if current_movie.release_date:
        #     count = 0
        #     while count <= 3:
        #         imdb_movie = self.imdb.get_movie(search_list[count].movieID)
        #         if current_movie.release_date != imdb_movie['year']:
        #             print(f'Incorrect: {imdb_movie["long imdb canonical title"]}')
        #             count += 1
        #         elif current_movie.release_date == imdb_movie['year']:
        #             print(f'Correct: {imdb_movie["long imdb canonical title"]}')
        #             return imdb_movie
        first_movie = self.imdb.get_movie(search_list[0].movieID)
        return first_movie

    def substitute_db_movie_info(self, imdb_movie, current_movie):
        logging.info(f'Calling {inspect.stack()[0][3]} module')

        movie = Movie.objects.get(pk=current_movie.id)
        print(imdb_movie.get('plot outline'))

        # 'actors': 'cast',
        # 'directed by': 'director',
        # 'created by': 'creator',
        # 'genre': 'genres',
        # 'runtime': 'runtimes',
        # 'writing credits': 'writer',
        # 'produced by': 'producer',
        # 'seasons': 'number of seasons',
        # 'language': 'languages',
        # 'videoclips': 'video clips',
        # 'photographs': 'photo sites',
        movie.country = imdb_movie['country'][0]
        movie.description = imdb_movie.get('plot outline')
        movie.duration = imdb_movie['runtime'][0]
        movie.poster_url = imdb_movie['full-size cover url']
        # movie.is_scraped = True
        if not movie.release_date:
            movie.release_date = imdb_movie['year']
        movie.save()

    def run(self):
        """
        Queue, threading cycle
        """
        filtered_movies = self.get_filter_db_movies()

        for movie in filtered_movies[:1]:
            imdb_search_list = self.search_imdb_movie(movie)
            imdb_movie = self.get_validate_search_list_movie(imdb_search_list, movie)

            try:
                self.substitute_db_movie_info(imdb_movie, movie)
            except Exception as e:
                logging.exception(e)


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)-24s: %(levelname)-8s %(message)s')
    start = datetime.now()

    imdb_scraper = IMDBScraper()
    imdb_scraper.run()

    finish = datetime.now() - start
    logging.info(f'Done in: {finish}')


if __name__ == '__main__':
    main()
