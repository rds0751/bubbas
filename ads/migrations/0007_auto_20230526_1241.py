# Generated by Django 3.1.2 on 2023-05-26 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20230523_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='9WZHEV204L', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]