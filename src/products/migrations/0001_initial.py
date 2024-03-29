# Generated by Django 2.2.3 on 2019-07-03 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('full_info', models.TextField()),
                ('portion', models.FloatField()),
                ('is_liquid', models.BooleanField()),
                ('kilojoules', models.FloatField(default=-1.0)),
                ('calories', models.FloatField(default=-1.0)),
                ('proteins', models.FloatField(default=-1.0)),
                ('carbohydrates', models.FloatField(default=-1.0)),
                ('sugar', models.FloatField(default=-1.0)),
                ('fats', models.FloatField(default=-1.0)),
                ('saturated_fats', models.FloatField(default=-1.0)),
                ('monosaturated_fats', models.FloatField(default=-1.0)),
                ('polysaturated_fats', models.FloatField(default=-1.0)),
                ('cholesterol', models.FloatField(default=-1.0)),
                ('cellulose', models.FloatField(default=-1.0)),
                ('sodium', models.FloatField(default=-1.0)),
                ('pottasium', models.FloatField(default=-1.0)),
                ('percent_carbohydrates', models.IntegerField()),
                ('percent_fats', models.IntegerField()),
                ('percent_proteins', models.IntegerField()),
            ],
        ),
    ]
