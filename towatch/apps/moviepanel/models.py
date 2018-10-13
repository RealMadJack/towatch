from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

from ..utility.utils import get_unique_slug


class MoviePanel(TimeStampedModel):
    name = models.CharField(_('Movie Panel'), blank=False, max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('Movie Panel')  # self.name Panel
        verbose_name_plural = _('Movie Panels')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:panel', kwargs={'moviepanel_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(MoviePanel, self.name)
        return super().save(*args, **kwargs)


class MovieCategory(TimeStampedModel):
    moviepanel = models.ForeignKey(
        MoviePanel,
        null=True,
        on_delete=models.SET_NULL,
        related_name='moviecategories',
        related_query_name='%(class)s',
    )
    name = models.CharField(_('Movie Category'), blank=False, default='', max_length=255)
    slug = models.SlugField(default='', max_length=255, unique=True)

    class Meta:
        verbose_name = _('Movie Category')
        verbose_name_plural = _('Movie Categories')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:category', kwargs={
            'moviepanel_slug': self.moviepanel.slug,
            'moviecategory_slug': self.slug
        })

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)


class Movie(models.Model):
    pass


# class MovieRanking(models.Model):  # Abstract?
#     pass


# class Comment(models.Model):  # validate against spammers
#     pass


# class CommentRanking(models.Model):  # Abstract?
#     pass


# class Review(models.Model):  # comment with highest rank
#     pass
