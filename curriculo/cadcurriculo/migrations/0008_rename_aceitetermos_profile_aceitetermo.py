# Generated by Django 3.2.4 on 2021-06-20 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadcurriculo', '0007_alter_profile_linkedin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='aceitetermos',
            new_name='aceitetermo',
        ),
    ]
