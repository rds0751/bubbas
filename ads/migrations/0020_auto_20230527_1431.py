# Generated by Django 3.1.2 on 2023-05-27 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0019_auto_20230527_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='OVQCQA1Z93', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]