# Generated by Django 3.1.4 on 2021-07-06 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0008_auto_20210419_1813'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ('-rank',)},
        ),
        migrations.AlterModelOptions(
            name='study',
            options={'ordering': ('start_date',), 'verbose_name': 'Учеба', 'verbose_name_plural': 'Учебы'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='rank',
            field=models.FloatField(verbose_name='Уровень'),
        ),
    ]
