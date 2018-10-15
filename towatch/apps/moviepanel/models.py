from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices, FieldTracker
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

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
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:genre', kwargs={
            'moviepanel_slug': self.moviepanel.slug,
            'moviegenre_slug': self.slug
        })

    def save(self, *args, **kwargs):
        if not self.slug or self.name != self.tracker.previous('name'):
            self.slug = get_unique_slug(MovieGenre, self.name)
        return super().save(*args, **kwargs)


class Movie(TimeStampedModel):
    moviepanel = models.ForeignKey(
        MoviePanel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='movies',
        related_query_name='%(class)s',
    )
    moviegenre = models.ManyToManyField(MovieGenre)
    name = models.CharField(_('Name'), blank=False, default='', max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)
    country = models.CharField(_('Country'), blank=True, default='', max_length=255)
    description = models.TextField(_('Description'), blank=False, default='', max_length=512)
    duration = models.PositiveIntegerField(_('Duration'), blank=True, default=0)
    poster = models.ImageField(_('Poster'), blank=True, null=True, upload_to='posters')
    poster_url = models.URLField(_('Poster URL'), blank=True, default='', max_length=200)
    release_date = models.PositiveIntegerField(_('Release date'), blank=True, default=0)
    trailer = models.URLField(_('Trailer'), blank=True, default='', max_length=200)
    tracker = FieldTracker()
    # status = Choices()
    # producer = models.CharField()
    # directors = models.ManyToManyField(Person, through='Director')
    # actors = models.ForeignKey()
    # imdb_id = models.CharField('IMDB ID', max_length=10)
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
        if not self.slug or self.name != self.tracker.previous('name'):
            self.slug = get_unique_slug(Movie, self.name)
        return super().save(*args, **kwargs)


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
