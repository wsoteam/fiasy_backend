# Generated by Django 2.2.3 on 2019-07-12 07:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20190712_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='meal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Ingredient'),
        ),
    ]