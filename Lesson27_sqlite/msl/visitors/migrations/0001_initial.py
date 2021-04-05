# Generated by Django 3.1.7 on 2021-04-05 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('birthdate', models.DateTimeField(verbose_name='дата рождения')),
                ('gender', models.CharField(max_length=3)),
            ],
        ),
    ]
