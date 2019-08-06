from django.db import models


class ArticleCategory(models.Model):
    name = models.CharField(max_length=80, null=True, unique=True)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Article Category'
        verbose_name_plural = 'Article Categories'

    def __str__(self):
        if self.parent:
            return self.parent.name + '/' + self.name
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='article_image')
    date = models.DateField(auto_now=True)
    category = models.ForeignKey(
        ArticleCategory,
        null=True,
        related_name='articles',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.title
