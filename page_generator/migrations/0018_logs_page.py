# Generated by Django 3.1.4 on 2021-03-12 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_generator', '0017_logs'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='page',
            field=models.IntegerField(default=None),
        ),
    ]
