from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices, FieldTracker
from model_utils.fields import StatusField, MonitorField
from model_utils.models import TimeStampedModel

from .utils import get_unique_slug


class MoviePanel(TimeStampedModel):
    name = models.CharField(_('Panel name'), blank=False, default='', max_length=112)
    slug = models.SlugField(max_length=112, unique=True)
    tracker = FieldTracker()

    class Meta:
        verbose_name = _('Movie Panel')  # f'{self.name}'
        verbose_name_plural = _('Movie Panels')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:panel', kwargs={'moviepanel_slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.tracker.previous('name'):
            self.slug = get_unique_slug(MoviePanel, self.name)
        return super().save(*args, **kwargs)


class MovieGenre(TimeStampedModel):
    moviepanel = models.ForeignKey(
        MoviePanel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='moviegenres',
        related_query_name='%(class)s',
    )
    name = models.CharField(_('Movie Genre'), blank=False, default='', max_length=112)
    slug = models.SlugField(default='', max_length=112, unique=True)
    tracker = FieldTracker()

    class Meta:
        verbose_name = _('Movie Genre')
        verbose_name_plural = _('Movie Genres')

    def __str__(self):
        return f'{self.name} : {self.moviepanel}'

    def get_absolute_url(self):
        return reverse('moviepanel:genre', kwargs={
            'moviepanel_slug': self.moviepanel.slug,
            'moviegenre_slug': self.slug
        })

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.tracker.previous('name'):
            self.slug = get_unique_slug(MovieGenre, self.name)
        return super().save(*args, **kwargs)


# class IMDB(TimeStampedModel):
#     pass


class Movie(TimeStampedModel):
    moviepanel = models.ForeignKey(
        MoviePanel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movies',
        related_query_name='%(class)s',
    )
    moviegenre = models.ManyToManyField(MovieGenre, related_name='movies')
    name = models.CharField(_('Name'), blank=False, default='', max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)
    actors = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    country = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    description = models.TextField(_('Description'), blank=False, default='', max_length=1024)
    duration = models.PositiveIntegerField(_('Duration'), blank=True, null=True, default=0)
    original_language = ArrayField(models.CharField(max_length=255), blank=True, default=list)
    poster = models.ImageField(_('Poster'), blank=True, null=True, upload_to='posters')
    poster_url = models.URLField(_('Poster URL'), blank=True, default='', max_length=200)
    rating = models.FloatField(_('Rating'), blank=True, default=0.0)
    release_date = models.PositiveIntegerField(_('Release date'), blank=True, default=0)
    seasons = models.PositiveIntegerField(_('Seasons'), blank=True, null=True, default=0)
    STATUS = Choices('invisible', 'visible')
    status = StatusField()
    published_at = MonitorField(monitor='status', when=['visible'])
    trailer = models.URLField(_('Trailer url'), blank=True, default='', max_length=200)
    yt_trailer_id = ArrayField(models.CharField(max_length=55), blank=True, default=list)
    tracker = FieldTracker()
    is_scraped = models.BooleanField(_('Is scraped'), default=False)
    # producer = models.CharField()
    # directors = models.ManyToManyField(Person, through='Director')
    # moviegenre = models.ManyToMany()
    # movieplayer = models.URLField()
    # rating = models.PositiveIntegerField()
    # review = models.ForeignKey(MovieReview, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:movie', kwargs={
            'moviepanel_slug': self.moviepanel.slug,
            'movie_slug': self.slug
        })

    def save(self, *args, **kwargs):
        """
        TODO: if moviegenre did not match with moviepanel = abort
        """
        if not self.slug or self.name != self.tracker.previous('name'):
            self.slug = get_unique_slug(Movie, self.name)
        return super().save(*args, **kwargs)


# class MoviePlayer(models.Model):  # Abstract?
#     pass  # o2m


# class MovieRanking(models.Model):  # Abstract?
#     pass


# class Comment(models.Model):  # validate against spammers
#     pass


# class CommentRanking(models.Model):  # Abstract?
#     pass


# class Review(models.Model):  # comment with highest rank
#     movie = models.ForeignKey(Movie, related_name='reviews')
#     user = models.ForeignKey(User)
#     comment = models.TextField()
#     rating = models.IntegerField(default=1,
#                                 validators=[
#                                     MaxValueValidator(5),
#                                     MinValueValidator(1)
#                                 ])
#     created_date = models.DateField(default=timezone.now)

#     def __str__(self):
#         return self.comment
