# Generated by Django 3.1.7 on 2021-04-05 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0003_auto_20210405_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitor',
            old_name='first',
            new_name='first_name',
        ),
    ]