# Generated by Django 2.0.6 on 2019-03-26 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exsercises', '0005_auto_20190325_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choseanswerexsercise',
            old_name='question',
            new_name='audio',
        ),
        migrations.AddField(
            model_name='choseanswerexsercise',
            name='image',
            field=models.TextField(blank=True, null=True),
        ),
    ]
