# Generated by Django 3.1.5 on 2021-01-27 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0025_auto_20210122_2015'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='director_yata',
            field=models.BooleanField(default=True),
        ),
    ]
