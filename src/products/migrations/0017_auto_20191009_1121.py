# Generated by Django 2.2.6 on 2019-10-09 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_auto_20191009_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='full_info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Full info'),
        ),
        migrations.AddField(
            model_name='brand',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=80, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='category',
            name='parent_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.Category', verbose_name='Parent'),
        ),
        migrations.AddField(
            model_name='measurementunit',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='product',
            name='full_info_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Full info'),
        ),
        migrations.AddField(
            model_name='product',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
    ]
