# Generated by Django 2.2.28 on 2023-12-18 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_alter_sales_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assortment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='geography',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='sales',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
