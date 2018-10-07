from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

from ..utility.utils import get_unique_slug


class MoviePanel(TimeStampedModel):
    name = models.CharField(_('Movie Panel'), blank=True, max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name = _('Movie Panel')
        verbose_name_plural = _('Movie Panels')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moviepanel:panel', kwargs={'moviepanel_slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = get_unique_slug(MoviePanel, self.name)
        return super().save(*args, **kwargs)


class MovieCategory(models.Model):
    pass


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
