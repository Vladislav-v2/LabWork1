# Generated by Django 2.1.7 on 2019-04-11 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appdatabase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='human',
            name='salary',
            field=models.IntegerField(),
        ),
    ]
