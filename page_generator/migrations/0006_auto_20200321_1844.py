# Generated by Django 3.0.2 on 2020-03-21 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_generator', '0005_auto_20200321_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagerating',
            name='credibility',
            field=models.IntegerField(choices=[(-3, 'Úplne nedôveryhodný'), (-2, 'Dosť nedôveryhodný'), (-1, 'Trochu nedôveryhodný'), (0, 'Neviem posúdiť'), (1, 'Trochu dôveryhodný'), (2, 'Dosť dôveryhodný'), (3, 'Úplne dôveryhodný')], default=None),
        ),
    ]
