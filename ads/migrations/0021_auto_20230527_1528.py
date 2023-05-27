# Generated by Django 3.1.2 on 2023-05-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0020_auto_20230527_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='0OL8KF8FM4', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
    ]