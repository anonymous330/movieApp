# Generated by Django 3.0.5 on 2020-06-14 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20200614_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymovie',
            name='flag',
            field=models.BooleanField(default=0, verbose_name=True),
            preserve_default=False,
        ),
    ]
