# Generated by Django 3.2.4 on 2021-06-14 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadcurriculo', '0002_auto_20210613_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instituicao',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='escolaridade',
            field=models.CharField(blank=True, choices=[('fundai', 'Fundamental Incompleto'), ('fundac', 'Fundamental Completo'), ('medioi', 'Ensino Médio Completo'), ('medioc', 'Ensino Médio Incompleto'), ('superi', 'Superior Incompleto'), ('superc', 'Superior Completo'), ('posgra', 'Pós-Graduação')], max_length=6, null=True, verbose_name='Grau de escolaridade'),
        ),
    ]
