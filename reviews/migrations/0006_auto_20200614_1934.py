# Generated by Django 3.0.5 on 2020-06-14 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20200614_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymovie',
            name='flag',
            field=models.BooleanField(verbose_name=False),
        ),
    ]
