# Generated by Django 3.1.2 on 2023-05-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0008_auto_20230526_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='profile_status',
            field=models.CharField(choices=[('Call Girl', 'Call Girl'), ('Escort', 'Escort')], default='Enabled', max_length=25),
        ),
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='9C4DA7J0S8', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
    ]