# Generated by Django 3.1.5 on 2021-04-14 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='requirements',
            new_name='requirement',
        ),
    ]
