# Generated by Django 2.0.5 on 2019-04-30 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_auto_20190426_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='awardsUpda',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='bazaarUpda',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='factionUpda',
            field=models.IntegerField(default=0),
        ),
    ]
