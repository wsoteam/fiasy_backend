# Generated by Django 2.2.3 on 2019-07-13 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0009_auto_20190712_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='portion',
            field=models.FloatField(default=100),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, to='products.Product'),
        ),
    ]
