# Generated by Django 2.2.3 on 2019-07-04 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190703_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('full_info', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='products.Brand'),
        ),
    ]