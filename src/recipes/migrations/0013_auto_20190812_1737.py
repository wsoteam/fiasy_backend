# Generated by Django 2.2.4 on 2019-08-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20190716_1715'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_process',
            field=models.TextField(blank=True, verbose_name='Cooking process'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Cooking time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date',
            field=models.DateField(auto_now=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='full_info',
            field=models.TextField(blank=True, verbose_name='Full info'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='recipe_image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='is_moderated',
            field=models.BooleanField(default=False, verbose_name='Is moderated'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='products.Product', verbose_name='Products'),
        ),
    ]
