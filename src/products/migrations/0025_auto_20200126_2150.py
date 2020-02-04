# Generated by Django 2.2.8 on 2020-01-26 19:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_auto_20200124_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='favorited_by',
            field=models.ManyToManyField(blank=True, related_name='favorite_products', to=settings.AUTH_USER_MODEL),
        ),
    ]