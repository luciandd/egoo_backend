# Generated by Django 2.0.6 on 2018-07-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='order',
            field=models.IntegerField(),
        ),
    ]