# Generated by Django 3.1.4 on 2021-02-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_auto_20210206_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='description',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projectimage',
            name='title',
            field=models.CharField(max_length=125, null=True),
        ),
    ]