# Generated by Django 2.2.7 on 2019-11-08 06:51

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0017_auto_20191105_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='title_color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
