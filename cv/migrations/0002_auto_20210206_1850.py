# Generated by Django 3.1.4 on 2021-02-06 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='role',
            field=models.CharField(max_length=125, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(null=True),
        ),
    ]