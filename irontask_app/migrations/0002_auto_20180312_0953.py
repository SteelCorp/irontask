# Generated by Django 2.0.3 on 2018-03-12 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irontask_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='email',
            field=models.EmailField(default='hhoutmann@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='siret',
            field=models.IntegerField(max_length=14, primary_key=True, serialize=False, verbose_name='Siret'),
        ),
    ]
