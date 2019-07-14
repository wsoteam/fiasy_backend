# Generated by Django 2.2.3 on 2019-07-14 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20190713_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_process',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(blank=True, to='products.Product'),
        ),
    ]