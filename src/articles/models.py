from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='article_image')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
