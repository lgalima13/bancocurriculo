# Generated by Django 3.2.4 on 2021-06-14 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadcurriculo', '0004_auto_20210613_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aceitetermos',
            field=models.BooleanField(default=False),
        ),
    ]