# Generated by Django 3.2.8 on 2023-06-07 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0043_ad_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='rank',
            field=models.IntegerField(default=10),
        ),
    ]