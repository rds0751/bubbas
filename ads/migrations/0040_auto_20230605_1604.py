# Generated by Django 3.2.8 on 2023-06-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0039_auto_20230605_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]