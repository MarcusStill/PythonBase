# Generated by Django 3.1.7 on 2021-04-05 21:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='birthdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]