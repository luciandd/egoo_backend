# Generated by Django 2.0.6 on 2019-03-31 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exsercises', '0007_auto_20190330_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='rewritesentenceexsercise',
            name='audio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='translatesentenceexsercise',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
