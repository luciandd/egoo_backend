# Generated by Django 2.0.6 on 2019-04-13 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readings', '0003_auto_20190401_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='explain',
            field=models.TextField(blank=True, null=True),
        ),
    ]
