# Generated by Django 3.0 on 2023-06-02 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0031_auto_20230602_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(to='ads.Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='images',
            field=models.ManyToManyField(to='ads.Image'),
        ),
    ]
