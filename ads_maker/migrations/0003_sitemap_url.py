# Generated by Django 3.1.1 on 2020-09-29 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_maker', '0002_auto_20200929_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitemap',
            name='url',
            field=models.URLField(default='sitemap.xml', help_text='xxx', unique=True),
            preserve_default=False,
        ),
    ]
