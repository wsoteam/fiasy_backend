# Generated by Django 2.2.3 on 2019-07-09 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20190709_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
    ]
