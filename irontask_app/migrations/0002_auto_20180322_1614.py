# Generated by Django 2.0.3 on 2018-03-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irontask_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benevole',
            name='sexe',
            field=models.CharField(choices=[('Feminin', 'F'), ('Masculin', 'M')], max_length=30),
        ),
    ]
