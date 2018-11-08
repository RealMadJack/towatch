import logging
import inspect
import re
import requests
import time
import threading
import sys
import os
import django

from bs4 import BeautifulSoup
from datetime import datetime
from imdb import IMDb

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__name__))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from towatch.apps.moviepanel.models import Movie


# Logging restrictions
logging.getLogger("imdbpy").setLevel(logging.WARNING)
logging.getLogger("imdb.parser.http.piculet").setLevel(logging.WARNING)
logging.getLogger("chardet.charsetprober").setLevel(logging.WARNING)


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

    def search_imdb_movie(self, movie):
        result = self.imdb.search_movie(movie.name)
        return result

    def get_validate_search_list_movie(self, search_list, current_movie):
        logging.info(f'Calling {inspect.stack()[0][3]} module')

        # print(f'Current movie date: {current_movie.release_date}')
        # print(first_movie['year'])
        # print(first_movie['long imdb canonical title'])

        if current_movie.release_date:
            count = 0
            while count <= 5:
                imdb_movie = self.imdb.get_movie(search_list[count].movieID)
                if current_movie.release_date != imdb_movie['year']:
                    logging.info(f'Incorrect: {imdb_movie["long imdb canonical title"]}')
                    count += 1
                elif current_movie.release_date == imdb_movie['year']:
                    logging.info(f'Correct: {imdb_movie["long imdb canonical title"]}')
                    return imdb_movie
        first_movie = self.imdb.get_movie(search_list[0].movieID)
        return first_movie

    def substitute_db_movie_info(self, imdb_movie, current_movie):
        """
        TODO: genres, images
        """
        logging.info(f'Calling {inspect.stack()[0][3]} module')

        # print(imdb_movie['seasons'])
        # 'genre': 'genres',
        movie = Movie.objects.get(pk=current_movie.id)

        movie.actors = imdb_movie.get('cast')[:5]
        movie.country = imdb_movie.get('country')
        movie.description = imdb_movie.get('plot outline')
        movie.duration = imdb_movie.get('runtime', 0)[0]
        movie.original_language = imdb_movie.get('language')
        movie.poster_url = imdb_movie.get('full-size cover url')
        movie.rating = imdb_movie.get('rating', 0.0)
        movie.seasons = imdb_movie.get('seasons', 0)
        movie.release_date = imdb_movie.get('year', 0)
        movie.is_scraped = True
        movie.save()

    def run(self):
        """
        TODO: Queue, threading cycle
        """
        filtered_movies = self.get_filter_db_movies()

        for movie in filtered_movies:
            imdb_search_list = self.search_imdb_movie(movie)
            imdb_movie = self.get_validate_search_list_movie(imdb_search_list, movie)

            try:
                self.substitute_db_movie_info(imdb_movie, movie)
            except Exception as e:
                logging.exception(e)


class YTScraper:
    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')

    def get_filter_db_movies(self):
        logging.info(f'Calling {inspect.stack()[0][3]} module')
        movies = Movie.objects.filter(is_yt_scraped=False)
        return movies

    def search_yt_trailer_id(self, movie):
        logging.info(f'Calling {inspect.stack()[0][3]} module')
        trailer = 'trailer'
        yt_query = f'https://www.youtube.com/results?search_query={movie.name}+{movie.release_date}+{trailer}'

        resp = requests.get(yt_query)
        soup = BeautifulSoup(resp.content, 'html.parser')
        search_list = soup.select('a.yt-uix-tile-link')[:10]
        search_validators = [movie.name.lower(), trailer.lower()]
        first_videoID = str(search_list[0]['href'][9:])
        result = []

        for video in search_list:
            if all(x in video['title'].lower() for x in search_validators):
                videoID = str(video['href'][9:])
                result.append(videoID)

        if len(result) == 0:
            result.append(first_videoID)
        return result

    def validate_search_list_result(self):
        """
        TODO: Thorough search_list validation by results length and different params
                (year, title, season)
        """
        logging.info(f'Calling {inspect.stack()[0][3]} module')

    def substitute_db_movie_trailer(self, search_list, current_movie):
        """
        TODO: is_yt_scraped = False if no results
        """
        logging.info(f'Calling {inspect.stack()[0][3]} module')
        movie = Movie.objects.get(pk=current_movie.id)
        movie.yt_trailer_id = search_list[:5]
        movie.is_yt_scraped = True
        movie.save()

    def run(self):
        logging.info(f'Calling {inspect.stack()[0][3]} module')
        filtered_movies = self.get_filter_db_movies()

        for movie in filtered_movies:
            yt_search_list = self.search_yt_trailer_id(movie)
            self.substitute_db_movie_trailer(yt_search_list, movie)


class MovieScraper:
    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')


class SerialScraper:
    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')


class AnimeScraper:
    def __init__(self):
        logging.info(f'Creating instance: {self.__class__.__name__}')


def main():
    logging.basicConfig(level=logging.DEBUG, format='%(name)-24s: %(levelname)-8s %(message)s')
    start = datetime.now()

    # imdb_scraper = IMDBScraper()
    # imdb_scraper.run()
    yt_scraper = YTScraper()
    yt_scraper.run()

    finish = datetime.now() - start
    logging.info(f'Done in: {finish}')


if __name__ == '__main__':
    main()
