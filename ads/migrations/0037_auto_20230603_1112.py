# Generated by Django 3.0 on 2023-06-03 05:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0036_auto_20230602_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='page_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]