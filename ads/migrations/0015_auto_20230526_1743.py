# Generated by Django 3.1.2 on 2023-05-26 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0014_auto_20230526_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='user',
        ),
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='1ZEE1AWV89', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]