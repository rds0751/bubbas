# Generated by Django 3.2.19 on 2023-06-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0029_auto_20230601_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='categories',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, to='ads.Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='content',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='featured',
            field=models.BooleanField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='id',
            field=models.BigAutoField(db_index=True, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='images',
            field=models.ManyToManyField(blank=True, db_index=True, null=True, to='ads.Image'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='likes',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='meta_description',
            field=models.TextField(blank=True, db_index=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='meta_title',
            field=models.TextField(blank=True, db_index=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='overview',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='phone',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='profile_status',
            field=models.CharField(blank=True, choices=[('Call Girls', 'Call Girls'), ('Escorts', 'Escorts')], db_index=True, default='Enabled', max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='thumbnail',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ad',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(blank=True, db_index=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='views',
            field=models.IntegerField(blank=True, db_index=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='ad',
            name='whatsapp',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='profile_picture',
            field=models.ImageField(blank=True, db_index=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='city',
            name='meta_description',
            field=models.TextField(blank=True, db_index=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='meta_title',
            field=models.TextField(blank=True, db_index=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='page_content',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='status',
            field=models.CharField(blank=True, choices=[('Enabled', 'Enabled'), ('Disabled', 'Disabled')], db_index=True, default='Enabled', max_length=10, null=True),
        ),
    ]
