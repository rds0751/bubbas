# Generated by Django 3.1.2 on 2023-05-26 11:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_auto_20230526_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.agency'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='ads.Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.city'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='featured',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.CharField(default='1OHJD7QXPN', max_length=15, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='ads.Image'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='meta_description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='meta_title',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='overview',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='profile_status',
            field=models.CharField(blank=True, choices=[('Call Girls', 'Call Girls'), ('Escorts', 'Escorts')], default='Enabled', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ad',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
