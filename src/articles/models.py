from django.db import models

from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_("First Name"), max_length=80, null=True)
    last_name = models.CharField(_("Last Name"), max_length=80, null=True)
    photo = models.ImageField(
        _('Author photo'),
        upload_to='author_photo',
        blank=True
    )
    bio = models.TextField(_("Biography"), blank=True)
    social_url = models.URLField(_("Social Media URL"), blank=True, null=True)
    achievement_1 = models.TextField(
        _("Achievement #1"),
        blank=True,
        null=True
    )
    achievement_2 = models.TextField(
        _("Achievement #2"),
        blank=True,
        null=True
    )
    achievement_3 = models.TextField(
        _("Achievement #3"),
        blank=True,
        null=True
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class ArticleSeries(models.Model):
    name = models.CharField(_("Name"), max_length=80, null=True, unique=True)
    users = models.ManyToManyField(
        User,
        related_name='article_series',
        blank=True,
    )

    def __str__(self):
        return self.name


class ArticleCategory(models.Model):
    name = models.CharField(_("Name"), max_length=80, null=True, unique=True)
    parent = models.ForeignKey(
        'self',
        verbose_name=_("Parent"),
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Article Category')
        verbose_name_plural = _('Article Categories')

    def __str__(self):
        if self.parent:
            return self.parent.name + '/' + self.name
        return self.name


class Article(models.Model):
    title = models.CharField(_('Title'), max_length=200)
    body = models.TextField(_('Body'))
    image = models.ImageField(
        _('Image'),
        upload_to='article_image',
        blank=True
    )
    premium = models.BooleanField(_('Premium'), default=False)
    date = models.DateField(_('Date'), auto_now=True)
    author = models.ForeignKey(
        Author,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    series = models.ForeignKey(
        ArticleSeries,
        verbose_name=_("Article Series"),
        null=True,
        blank=True,
        related_name='article_series',
        on_delete=models.PROTECT
    )
    day_in_series = models.IntegerField(
        _('Day in Series'),
        choices=((int(x), x) for x in range(1, 32)),
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        ArticleCategory,
        verbose_name=_("Category"),
        null=True,
        blank=True,
        related_name='articles',
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')

    def __str__(self):
        return self.title
