# Generated by Django 3.1.4 on 2020-12-12 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Учеба')),
                ('name_ru', models.CharField(max_length=150, null=True, verbose_name='Учеба')),
                ('name_en', models.CharField(max_length=150, null=True, verbose_name='Учеба')),
                ('name_de', models.CharField(max_length=150, null=True, verbose_name='Учеба')),
            ],
            options={
                'verbose_name': 'Учеба',
                'verbose_name_plural': 'Учебы',
            },
        ),
    ]