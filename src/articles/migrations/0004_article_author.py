# Generated by Django 2.2.5 on 2019-09-23 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190812_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=80, null=True, verbose_name='Author'),
        ),
    ]
