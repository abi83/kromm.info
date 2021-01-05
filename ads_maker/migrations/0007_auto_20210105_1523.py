# Generated by Django 3.1.4 on 2021-01-05 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads_maker', '0006_sitemap_is_sm_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ('-updated_at',)},
        ),
        migrations.AddField(
            model_name='site',
            name='short_desc',
            field=models.TextField(default='Default short_desc', max_length=1023, verbose_name='Some Description'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='site',
            name='url',
            field=models.URLField(unique=True),
        ),
        migrations.AlterField(
            model_name='sitemap',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='site', to='ads_maker.site'),
        ),
    ]
