# Generated by Django 2.1.1 on 2018-09-19 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showtimefinder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='dateofbirth',
            field=models.DateField(default='2000-08-10'),
        ),
    ]