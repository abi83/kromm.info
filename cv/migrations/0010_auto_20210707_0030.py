# Generated by Django 3.1.4 on 2021-07-06 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_auto_20210706_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='rank_de',
            field=models.CharField(max_length=25, null=True, verbose_name='Опыт'),
        ),
        migrations.AddField(
            model_name='skill',
            name='rank_en',
            field=models.CharField(max_length=25, null=True, verbose_name='Опыт'),
        ),
        migrations.AddField(
            model_name='skill',
            name='rank_ru',
            field=models.CharField(max_length=25, null=True, verbose_name='Опыт'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='rank',
            field=models.CharField(max_length=25, verbose_name='Опыт'),
        ),
    ]
