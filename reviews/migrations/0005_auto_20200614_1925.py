# Generated by Django 3.0.5 on 2020-06-14 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_mymovie_flag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymovie',
            name='flag',
            field=models.BooleanField(),
        ),
    ]
