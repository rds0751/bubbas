# Generated by Django 3.1.2 on 2023-05-27 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0025_auto_20230527_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]