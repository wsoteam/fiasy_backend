# Generated by Django 2.2.3 on 2019-07-09 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20190709_1746'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together={('parent',)},
        ),
    ]
