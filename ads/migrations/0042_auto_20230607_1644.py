# Generated by Django 3.2.8 on 2023-06-07 11:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0041_rename_page_content_city_call_girl_page_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='call_girl_page_content',
            new_name='call_girls_page_content',
        ),
        migrations.AddField(
            model_name='city',
            name='escorts_page_content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
