# Generated by Django 4.2.7 on 2023-12-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assortment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=50)),
                ('seasonality', models.CharField(max_length=50)),
            ],
        ),
    ]
