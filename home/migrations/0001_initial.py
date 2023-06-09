# Generated by Django 3.1.2 on 2023-05-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, default='Enabled', max_length=25, null=True)),
                ('image', models.FileField(upload_to='')),
            ],
        ),
    ]
