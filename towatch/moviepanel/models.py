from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from model_utils import Choices
from model_utils.fields import StatusField
from model_utils.models import StatusModel, TimeStampedModel

from ..utility.utils import get_unique_slug


class MoviePanel(models.Model):
    pass


class MovieCategory(models.Model):
    pass


class Movie(models.Model):
    pass


class MovieRanking(models.Model):  # Abstract?
    pass


class Comment(models.Model):  # validate against spammers
    pass


class CommentRanking(models.Model):  # Abstract?
    pass


class Review(models.Model):  # comment with highest rank
    pass
