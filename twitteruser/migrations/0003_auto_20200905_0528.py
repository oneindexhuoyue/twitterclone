# Generated by Django 3.1.1 on 2020-09-05 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitteruser', '0002_auto_20200905_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='following',
            field=models.BooleanField(),
        ),
    ]
