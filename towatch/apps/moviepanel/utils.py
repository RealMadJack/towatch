from django.utils.text import slugify


def get_unique_slug(cls, name):
    """TODO: other unicode(ru) slugify"""

    slug = slugify(name)
    unique_slug = slug
    num = 1
    while cls.objects.filter(slug=unique_slug).exists():
        unique_slug = '{}-{}'.format(slug, num)
        num += 1
    return unique_slug
