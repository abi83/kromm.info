# Generated by Django 3.1.4 on 2021-02-03 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20210128_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_time',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='start_time',
            field=models.DateField(),
        ),
    ]
